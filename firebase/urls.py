from django.contrib import admin
from django.urls import path, include
from firebase.views import HomeView, AddEmployeeView
from firebase.utils.constants import Urls


urlpatterns = [
    path("admin/", admin.site.urls),
    path("accounts/", include("accounts.urls")),
    path("", HomeView.as_view(), name=Urls.HOME_REVERSE.value),
    path(
        "add_employee/", AddEmployeeView.as_view(), name=Urls.ADD_EMPLOYEE_REVERSE.value
    ),
]
