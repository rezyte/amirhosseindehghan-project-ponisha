from django.shortcuts import render
from django.views import generic
from django.contrib.auth import mixins

class CourseListView(mixins.LoginRequiredMixin, generic.ListView):
    template_name = "course-list.html"
    
    def get_query_set(self, *args, **kwargs):
        return Profile.objects.get(user=self.request.user).courses.all()