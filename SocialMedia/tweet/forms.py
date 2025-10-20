from django import forms
from .models import Tweet

class TweetForm(forms.ModelForm):
    class Meta:
        model = Tweet
        fields = ('text', 'image')
        widgets = {
            'text': forms.Textarea(attrs={'row': 5, 'col': 60, 'placeholder': "Enter your tweet here...", 'class': "form-control"}),
            'image': forms.FileInput(attrs={'class': "form-control"})
        }