from django.db import models

from apps.core.models import TimeSpecificModelBase
# ICON_CHOICES = (
#     ("", ""),
#     ("", ""),
#     ("", ""),
# )

# COLOR_CHOICES = (
#     ("aqua", "Aqua Blue"),
#     ("green", "Green"),
#     ("yellow", "Mustard Yellow"),
# )
class Course(TimeSpecificModelBase, models.Model):
    # category = models.ForeignKey(Category, on_delete=models.CASCADE)
    title = models.CharField(max_length=2048, verbose_name="نام دوره")
    slug = models.SlugField(allow_unicode=True, verbose_name="نامک دوره")
    description = models.TextField(blank=True, verbose_name="توضیحات")
    image = models.ImageField(upload_to="categories", blank=True, verbose_name="عکس")
    is_active = models.BooleanField(default=True, verbose_name="فعال")
    # bg_color = models.CharField(max_length=18, default="aqua", verbose_name="رنگ پس زمینه")
    # ion_icon = models.CharFiedl(max_legnth=290, default="aqua", verbose_name="آیکون دوره")

    class Meta:
        verbose_name_plural = "دوره ها"

    def __str__(self):
        return self.title