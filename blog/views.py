from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from rest_framework import viewsets
from rest_framework import permissions

from blog.models import Blog
from blog.serializers import BlogSerializer

# Create your views here.


class BlogView(viewsets.ModelViewSet):
    """
    Authentication View
    """

    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
    permission_classes = [permissions.IsAuthenticated]

    def handle_exception(self, exc):
        data = {
            "success": False,
            "message": exc.__str__()
        }

        return Response(data, status=status.HTTP_401_UNAUTHORIZED)

    def create(self, request, format=None):
        payload = request.data
        payload['user_id'] = request.user.id

        serializer = BlogSerializer(data=request.data)
        if(serializer.is_valid()):
            serializer.save()
            obj = {
                "success": True,
                "message": "Blog created Successfully!"
            }
            return Response(obj, status=status.HTTP_201_CREATED)
        obj = {
            "success": False,
            "message": serializer.errors
        }
        return Response(obj, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk, format=None):
        user = request.user

        queryset = Blog.objects.filter(user_id=user.id).get(pk=pk)
        if not queryset:
            obj = {
                "success": False,
                "message": "Blog Not Found!"
            }
            return Response(obj, status=status.HTTP_401_UNAUTHORIZED)

        serializer = BlogSerializer(queryset)
        obj = {
            "success": True,
            "data": serializer.data,
        }
        return Response(obj, status=status.HTTP_200_OK)

    def list(self, request, format=None):
        user = request.user

        queryset = Blog.objects.filter(user_id=user.id).all()

        serializer = BlogSerializer(queryset, many=True)
        obj = {
            "success": True,
            "data": serializer.data,
        }
        return Response(obj, status=status.HTTP_401_UNAUTHORIZED)

    def update(self, request, pk=None):
        user = request.user

        queryset = Blog.objects.filter(user_id=user.id).get(pk=pk)
        if not queryset:
            obj = {
                "success": False,
                "message": "Blog Not Found!"
            }
            return Response(obj, status=status.HTTP_401_UNAUTHORIZED)

        payload = request.data
        payload['user_id'] = user.id

        serializer = BlogSerializer(queryset, data=payload)
        if(serializer.is_valid()):
            serializer.save()
            obj = {
                "success": True,
                "message": "Blog Updated Successfully!"
            }
            return Response(obj, status=status.HTTP_201_CREATED)
        obj = {
            "success": False,
            "message": serializer.errors,
        }
        return Response(obj, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk, format=None):
        user = request.user

        queryset = Blog.objects.filter(user_id=user.id).get(pk=pk)
        if not queryset:
            obj = {
                "success": False,
                "message": "Blog Not Found!"
            }
            return Response(obj, status=status.HTTP_401_UNAUTHORIZED)

        queryset.delete()

        obj = {
            "success": True,
            "message": "Blog Deleted"
        }
        return Response(obj, status=status.HTTP_200_OK)
