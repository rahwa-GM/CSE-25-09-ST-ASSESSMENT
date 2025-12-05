from django import forms
from .models import Song
import datetime, mimetypes

class SongUploadForm(forms.ModelForm):
    class Meta:
        model = Song
        fields = ['cover', 'title', 'artist', 'album', 'year', 'audio']
        error_messages = {
            'title': {
                'required': "Title is required.",
                'max_length': "Title cannot exceed 100 characters."
            },
            'artist': {
                'required': "Artist is required.",
                'max_length': "Artist name cannot exceed 100 characters."
            },
            'album': {
                'required': "Album is required.",
                'max_length': "Album name cannot exceed 100 characters."
            },
            # 'year': {
            #     'required': "Year is required."
            # },
            'audio': {
                'required': "Audio file is required."
            },
        }

    # dynamic Bootstrap validation styling for your Django form
    # __init__ this method runs every time the form is created
    # Its purpose is to add or update CSS classes on each form field depending on: whether the form was submitted (is_bound) whether each field has an error or not
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field_name, field in self.fields.items(): # loop through all fields in your form    

            if self.is_bound:  # form was submitted
                if self.errors.get(field_name): # If the field has errors, adds Bootstrap's red outline
                    field.widget.attrs.update({
                        "class": "form-control is-invalid"
                    })
                else:
                    field.widget.attrs.update({  # If the field has NO errors, adds Bootstrap’s green outline
                        "class": "form-control is-valid"
                    })
            else:
                field.widget.attrs.update({ # When the form is not submitted, Initial display — no green/red colors.
                    "class": "form-control"
                })

    def clean_audio(self): # cleaned_data is a dictionary that holds all the validated and cleaned form input values after form.is_valid() has been called
        """Custom validation for the audio field"""
        audio = self.cleaned_data.get('audio')
        if audio:
            mime_type, _ = mimetypes.guess_type(audio.name)
            if mime_type not in ['audio/mpeg', 'audio/wav', 'audio/ogg']:
                raise forms.ValidationError("Unsupported audio file type.")
        return audio

    # def clean_year(self):
    #     """Custom validation for the year field"""
    #     year = self.cleaned_data.get('year')  
    #     if year > datetime.date.today().year:
    #         raise forms.ValidationError("Year cannot be in the future.")
    #     return year