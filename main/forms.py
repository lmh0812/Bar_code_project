from django import forms

from .models import Bar_code, Img, Imgadd

class PostForm(forms.ModelForm):

    class Meta:
        model = Bar_code
        fields = ('code', 'name', 'charge',)

class UploadForm(forms.ModelForm):
    
    class Meta:
        model = Img
        fields = ( 'title','image', )

class Post2Form(forms.ModelForm):

    class Meta:
        model = Imgadd
        fields = ('code_img', 'name', 'charge',)