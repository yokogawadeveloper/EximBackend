from django.urls import path
from .views import (RegisterView,LoginAPIView,LogoutView,)
from rest_framework_simplejwt.views import (TokenRefreshView,)

urlpatterns = [
    path("register/", RegisterView.as_view(), name="register"),
    path("login/", LoginAPIView.as_view(), name="login"),
    path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path('logout/', LogoutView.as_view(), name="logout"),
]
