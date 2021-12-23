from django.shortcuts import render
from django.views import generic
from django.contrib.auth import mixins

from apps.profiles.models import Profile
from apps.core.mixins import HasCompletedProfileAccessMixin
from .models import Course

class CourseListView(mixins.LoginRequiredMixin, HasCompletedProfileAccessMixin, generic.ListView):
    template_name = "course-list.html"

    def get_queryset(self, *args, **kwargs):
        return Profile.objects.get(user=self.request.user).courses.all()


class CourseDetailView(mixins.LoginRequiredMixin, HasCompletedProfileAccessMixin, generic.DetailView):
    template_name = "course-detail.html"
    model = Course

    def get_queryset(self):
        return Profile.objects.get(user=self.request.user).courses.all()
    