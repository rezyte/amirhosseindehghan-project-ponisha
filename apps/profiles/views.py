from django.shortcuts import render
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from apps.core.mixins import HasCompletedProfileAccessMixin


class ProfileIndexView(
    LoginRequiredMixin,
    HasCompletedProfileAccessMixin,
    View,
):

    def get(self, request, *args, **kwargs):
        return render(request, "profile.html", context = {})

    def post(self, request, *args, **kwargs):
        pass

class CompleteProfileView(
    LoginRequiredMixin,
    View,
):

    def get(self, request, *args, **kwargs):
        return render(request, "complete-profile.html", context={})

    def post(self, request, *args, **kwargs):
        # logic to complete profile
        pass