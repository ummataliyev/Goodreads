from django.urls import path

from users.views import LoginView
from users.views import LogoutView
from users.views import ProfileView
from users.views import RegisterView

app_name = "users"

urlpatterns = [
    path("login", LoginView.as_view(), name="login"),
    path("logout/", LogoutView.as_view(), name="logout"),
    path("profile/", ProfileView.as_view(), name="profile"),
    path("register", RegisterView.as_view(), name="register")
]
