# Generated by Django 3.0.5 on 2020-05-05 12:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogapp', '0009_remove_blogs_blog_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogs',
            name='blog_image',
            field=models.ImageField(default=1, upload_to='upload/', verbose_name='Blog Image'),
            preserve_default=False,
        ),
    ]
