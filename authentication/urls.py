from django.urls import path, include
# from app import views
from rest_framework_simplejwt.views import TokenRefreshView
from authentication.views import PersonView, PersonAuthViewSet

login = PersonAuthViewSet.as_view({
    'post': 'login',
})
register = PersonAuthViewSet.as_view({
    'post': 'register'
})
redirect = PersonAuthViewSet.as_view({
    'get': 'redirectedMethod'
})

changePassword = PersonView.as_view({
    'post': 'changePassword'
})
checkAuth = PersonView.as_view({
    'get': 'get'
})
userinfo = PersonView.as_view({
    'get': 'userInfo'
})
logout = PersonView.as_view({
    'post': 'logout'
})


urlpatterns = [
    path('api/register', register, name='register'),
    path('api/login', login, name='login'),
    path('api/me', userinfo, name='userinfo'),
    path('api/change-password', changePassword, name='change-password'),
    path('auth/', include('rest_framework_social_oauth2.urls')),
    path('accounts/profile/', redirect, name='redirected-method'),
    path('api/refresh-token', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/home', checkAuth, name='check-auth'),
    path('api/logout', logout, name='logout')
]
