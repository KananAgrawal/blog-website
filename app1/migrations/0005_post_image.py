# Generated by Django 4.2.7 on 2024-02-03 19:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0004_post_delete_home'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='image',
            field=models.ImageField(default='default-blog-thumb.png', upload_to='blog_pics'),
        ),
    ]
