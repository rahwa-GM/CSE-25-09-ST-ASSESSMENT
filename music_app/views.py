from django.shortcuts import render, redirect
from .models import Song
from .forms import SongUploadForm
from django.contrib import messages # Import Django's messaging framework to display one-time notifications to users


# Create your views here.
def upload_and_list_songs(request):
    if request.method == "POST":
        # request.FILES This contains all the files uploaded (like cover images or audio files).
        # Django separates files from normal form data, so need to pass them separately
        form = SongUploadForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "Song uploaded successfully!")
            return redirect('music_app:home')  # reload page to update list
    else:
        form = SongUploadForm()


    # Get all songs for the list section
    songs = Song.objects.all().order_by('uploaded_at')     # ascending order → oldest first, newest last.
    
    return render(request, 'music_app/song.html', {'form': form, 'songs': songs})

