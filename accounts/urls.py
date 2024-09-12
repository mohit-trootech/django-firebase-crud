from django.urls import path, include
from firebase import views
from accounts.views import LoginView, LogOutView, RegisterView
from accounts.utils.constants import Urls

urlpatterns = [
    path("login/", LoginView.as_view(), name=Urls.LOGIN_REVERSE.value),
    path("register/", RegisterView.as_view(), name=Urls.REGISTER_REVERSE.value),
    path("logout/", LogOutView.as_view(), name=Urls.LOGOUT_REVERSE.value),
]
