from django.db import models

from apps.core.models import TimeSpecificModelBase

class Course(TimeSpecificModelBase, models.Model):
    # category = models.ForeignKey(Category, on_delete=models.CASCADE)
    title = models.CharField(max_length=2048, verbose_name="نام دوره")
    slug = models.SlugField(allow_unicode=True, verbose_name="نامک دوره")
    description = models.TextField(blank=True, verbose_name="توضیحات")
    image = models.ImageField(upload_to="categories", blank=True, verbose_name="عکس")
    is_active = models.BooleanField(default=True, verbose_name="فعال")

    def __str__(self):
        return self.title