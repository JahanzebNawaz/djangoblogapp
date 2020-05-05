from django import forms
from .models import Blogs
from ckeditor.fields import RichTextFormField
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class BlogsForm(forms.ModelForm):
        '''
                Forms for Blogs
        '''

        class Meta:
                model = Blogs
                fields = ['blog_title', 'blog_description', 'blog_image']
                widgets = {
                        'blog_title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Blog Title'}),
                        'blog_description': RichTextFormField(),
                        'blog_image': forms.FileInput(attrs={'class': 'custom-file-input'}),
                }


class SignupForm(UserCreationForm):
        class Meta:
                model = User
                fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']
                widgets = {
                        'username': forms.TextInput(attrs={'class': 'form-control'}),
                        'first_name': forms.TextInput(attrs={'class': 'form-control'}),
                        'last_name': forms.TextInput(attrs={'class': 'form-control'}),
                        'email': forms.TextInput(attrs={'class': 'form-control'}),
                }
        
        def __init__(self, *args, **kwargs):
                super(SignupForm, self).__init__(*args, **kwargs)
                self.fields['password1'].widget.attrs['class'] = 'form-control'
                self.fields['password2'].widget.attrs['class'] = 'form-control'
