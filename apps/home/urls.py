from django.urls import path
from . import views

app_name = "home"

urlpatterns = [
    path('', views.index),
    path('signin', views.LoginView.as_view(), name="login"),
    path('profile', views.ProfileView.as_view(), name="profile"),
    path('panel', views.panel)
]