"""
URL configuration for music project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings        # for settings.DEBUG, MEDIA_URL, MEDIA_ROOT
from django.conf.urls.static import static  # for serving media files

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('music_app.urls')),  # namespace comes from music_app/urls.py

]

if settings.DEBUG: # serving media files during development
    # URL patterns for serving media files (uploads) during development.
    # MEDIA_URL is the URL prefix for media files, e.g., /media/.
    # MEDIA_ROOT is the folder on your filesystem where media files are stored, e.g., BASE_DIR / 'media'.
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

    
    # If a user visits http://localhost:8000/media/myfile.jpg, Django will look in MEDIA_ROOT and serve myfile.jpg