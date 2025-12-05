from django.db import models
from django.core.exceptions import ValidationError # imports Django’s ValidationError, which is used to raise errors when data fails validation
import datetime  # Python’s standard datetime module, which lets you work with dates and times in Django models
import mimetypes # importing Python’s built-in mimetypes module, which is used to guess the type of a file based on its name or extension




# Create your models here.
class Song(models.Model):
    # ImageField uses Pillow under the hood automatically.
    # Pillow is a Python imaging library
    cover = models.ImageField(upload_to='covers/', blank=True, null=True) # where to store uploaded files inside the MEDIA folder
    title = models.CharField(max_length=100)
    artist = models.CharField(max_length=100)
    album = models.CharField(max_length=100)
    year = models.PositiveIntegerField()
    audio = models.FileField(upload_to='audio/', null=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)  # <-- automatically set when a song is created

    def clean(self):
        """
        Custom validation for Song.
        """
        # year validation

         # YEAR VALIDATION
        if self.year is None:
            raise ValidationError({'year': "Year is required."})
        if self.year > datetime.date.today().year:
            raise ValidationError({'year': "Year cannot be in the future."})
        
        # audio validation
        if self.audio:
            mime_type, _ = mimetypes.guess_type(self.audio.name) # Uses Python’s built-in mimetypes module to guess the file type based on the file name/extension
            if mime_type not in ['audio/mpeg', 'audio/wav', 'audio/ogg']: # Checks if the guessed file type is one of the allowed audio types (mp3, wav, ogg)
                raise ValidationError({'audio': "Unsupported audio file type."})
   

    # the string representation of a model instance
    def __str__(self):
        return self.title