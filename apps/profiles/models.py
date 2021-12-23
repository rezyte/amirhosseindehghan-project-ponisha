from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    courses = models.ManyToManyField("courses.Course")
    phone = models.CharField(max_length=20)
    address = models.CharField(max_length=1024)
    has_completed = models.BooleanField(default=False)

    class Meta:
        verbose_name_plural = "پروفایل ها"

    def __str__(self):
        return f"profile for: {self.user.get_full_name()}"

    def save(self, *args, **kwargs):
        super(Profile, self).save(*args, **kwargs)
        if not self.has_completed and (self.user.email and self.user.first_name and self.user.last_name and self.user.email and self.phone and self.address):
            self.has_completed = True


