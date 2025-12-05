from django.urls import path # Import the path function to define URL routes for this app
from . import views # Import views from the current app to connect URL patterns with view functions

# Namespace tells Django all the URL names inside this file belong to this app
app_name = 'music_app' 

urlpatterns = [
    path('', views.upload_and_list_songs, name='home'),
]