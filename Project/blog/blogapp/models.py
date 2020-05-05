from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField

# Create your models here.

class Blogs(models.Model):
        '''
                Database Table for blogs
        '''
        blog_title = models.CharField(max_length=150, verbose_name='Blog Title')
        blog_description =RichTextField(max_length=2000, verbose_name='Description')
        blog_user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Blog User')
        blog_image = models.ImageField(upload_to='upload/', verbose_name='Blog Image')

        created_on = models.DateTimeField(auto_now=True)
        updated_on = models.DateTimeField(auto_now_add=True)

        def __str__(self):
                return self.blog_title