from django.urls import path
from . import views

urlpatterns = [
    path("main_page/", views.main_view, name="main_page"),
    path("login/", views.login_view, name="user_login"),
    path("register/", views.register_view, name="register_view"),
    path("admin_login/", views.admin_login_view, name="admin_login")
]
