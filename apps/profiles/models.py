from django.db import models
from django.contrib.auth import get_user_model
from django.db.models.signals import post_save
from django.dispatch import receiver

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
        if self.address and self.phone:
            if self.user.email and self.user.last_name:
                self.has_completed = True
        
        super(Profile, self).save(*args, **kwargs)

@receiver(post_save, sender=User)
def change_has_completed_status(sender, instance, created, **kwargs):
    instance.profile.save()
    print("Implemented save for this \n", instance.email, "email owner profile")

