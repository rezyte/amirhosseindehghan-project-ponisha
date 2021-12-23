from django.contrib import admin
from django.urls import path, include
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('apps.home.urls', namespace="home")),
    path('courses/', include('apps.courses.urls', namespace="courses")),
    path('videos/', include('apps.videos.urls', namespace="videos")),
    path('profile/', include('apps.profiles.urls', namespace="profiles")),
]


urlpatterns += staticfiles_urlpatterns()

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)