from django import forms
from .models import Post
from pyuploadcare.dj.forms import ImageField

class PostForm(forms.Form):
    pub_date = forms.CharField()
    content = forms.CharField()
    photo = ImageField(label='')

    class Meta:
        model = Post()
        fields = ('pub_date','content','photo')