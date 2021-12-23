from django.urls import path
from . import views

app_name = "profiles"

urlpatterns = [
    path("", views.ProfileIndexView.as_view(), name="index"),
    path("complete/", views.CompleteProfileView.as_view(), name="complete-info"),
]