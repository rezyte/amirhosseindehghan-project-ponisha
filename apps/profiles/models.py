from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    courses = models.ManyToManyField("courses.Course")

    def __str__(self):
        return f"profile for: {self.user.get_full_name()}"