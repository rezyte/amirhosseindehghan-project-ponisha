from django.db import models

from apps.core.models import TimeSpecificModelBase

class Video(TimeSpecificModelBase, models.Model):
    course = models.ForeignKey("courses.Course", on_delete=models.CASCADE)
    title = models.CharField(max_length=2048, verbose_name="نام دوره")
    slug = models.SlugField(allow_unicode=True, verbose_name="نامک")
    description = models.TextField(blank=True, verbose_name="توضیحات")
    image = models.ImageField(upload_to="categories", blank=True, verbose_name="عکس")
    is_active = models.BooleanField(default=True, verbose_name="فعال")
    order = models.PositiveIntegerField(blank=True, verbose_name="ترتیب")
    is_demo = models.BooleanField(
        default=False, verbose_name="دمو"
        help_text="ویدیو به صورت دمو قابل مشاده باشد"
    )

    class Meta:
        ordering = ["order"]

    def __str__(self):
        return self.title