from django.shortcuts import render
from django.views import generic
from django.contrib.auth import mixins

from apps.profiles.models import Profile
from .models import Course

class CourseListView(mixins.LoginRequiredMixin, generic.ListView):
    template_name = "course-list.html"
    
    def get_queryset(self, *args, **kwargs):
        return Profile.objects.get(user=self.request.user).courses.all()


class CourseDetailView(mixins.LoginRequiredMixin, generic.DetailView):
    template_name = "course-detail.html"
    model = Course

    def get_queryset(self):
        return Profile.objects.get(user=self.request.user).courses.all()
    