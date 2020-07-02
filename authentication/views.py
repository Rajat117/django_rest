from django.contrib.auth.hashers import check_password, make_password
from django.contrib.auth import logout
from django.shortcuts import redirect
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from rest_framework import viewsets
from rest_framework import permissions

from authentication.models import Person
from authentication.serializers import PersonSerializer, ChangePasswordSerializer
from authentication.utils import get_tokens_for_user

# Create your views here.


class PersonAuthViewSet(viewsets.ModelViewSet):
    """
    Authentication View
    """

    queryset = Person.objects.all()
    serializer_class = PersonSerializer

    def handle_exception(self, exc):
        data = {
            "success": False,
            "message": exc.__str__()
        }

        return Response(data, status=status.HTTP_401_UNAUTHORIZED)

    def register(self, request, format=None):
        serializer = PersonSerializer(data=request.data)
        if(serializer.is_valid()):
            serializer.save()
            obj = {
                "success": True,
                "message": "Successfully Registered!"
            }
            return Response(obj, status=status.HTTP_201_CREATED)
        obj = {
            "success": False,
            "message": serializer.errors,
        }
        return Response(obj, status=status.HTTP_400_BAD_REQUEST)

    def login(self, request, format=None):
        queryset = Person.objects.get(email=request.data['email'])
        if(check_password(request.data['password'], queryset.password)):
            token = get_tokens_for_user(queryset)
            obj = {
                "success": True,
                "data": token,
            }
            return Response(token, status=status.HTTP_200_OK)
        obj = {
            "success": False,
            "message": "Incorrect Password!"
        }
        return Response(obj, status=status.HTTP_401_UNAUTHORIZED)

    def redirectedMethod(self, request, format=None):
        queryset = Person.objects.get(pk=request.session['_auth_user_id'])

        token = get_tokens_for_user(queryset)
        refresh = 'refresh=' + token['refresh']
        access = 'access=' + token['access']
        request.session.flush()

        return redirect('https://easy-svelte.netlify.com/Social/Redirect?' +
                        refresh + '&' + access)


class PersonView(viewsets.ModelViewSet):
    """
    Authenticated View
    """

    queryset = Person.objects.all()
    serializer_class = PersonSerializer
    permission_classes = [permissions.IsAuthenticated]

    def handle_exception(self, exc):
        data = {
            "success": False,
            "message": exc.__str__()
        }

        return Response(data, status=status.HTTP_401_UNAUTHORIZED)

    def userInfo(self, request, format=None):
        queryset = Person.objects.get(email=request.user)
        queryset.password = None
        serializer = PersonSerializer(queryset)
        data = {
            "success": True,
            "data": serializer.data
        }
        return Response(data, status=status.HTTP_200_OK)

    def get(self, request, format=None):
        data = {
            "ok": True
        }
        return Response(data, status=status.HTTP_200_OK)

    def changePassword(self, request, format=None):
        serializer = ChangePasswordSerializer(data=request.data)
        if not (serializer.is_valid()):
            data = {
                "success": False,
                "message": serializer.errors,
            }
            return Response(data, status=status.HTTP_401_UNAUTHORIZED)

        queryset = Person.objects.get(email=request.user)
        queryset.password = make_password(request.data['new_password'])
        queryset.save()
        data = {
            "success": True,
            "message": "Password Changed!",
        }
        return Response(data, status=status.HTTP_200_OK)

    def logout(self, request, format=None):
        logout(request)
        return Response(status=status.HTTP_204_NO_CONTENT)
