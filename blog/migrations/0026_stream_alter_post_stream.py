# Generated by Django 5.0.7 on 2024-09-12 19:00

import django.db.models.deletion
from django.conf import settings
from django.db import migrations
from django.db import models

def set_stream(apps, schema_editor):
    Post = apps.get_model('blog', 'Post')
    Stream = apps.get_model('blog', 'Stream')

    for post in Post.objects.all():
        stream = Stream.objects.create(post=post, user=post.author, following=post.author)
        post.stream = stream
        post.save()


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0025_post_stream'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Stream',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('following', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='stream_following', to=settings.AUTH_USER_MODEL)),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='stream_post', to='blog.post')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AlterField(
            model_name='post',
            name='stream',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='stream_post', to='blog.stream'),
        ),
        migrations.RunPython(set_stream),
    ]
