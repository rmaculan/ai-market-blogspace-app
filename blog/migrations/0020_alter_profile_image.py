# Generated by Django 5.0.7 on 2024-09-07 00:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0019_profile_profilegroup_profile_groups_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.ImageField(default='', null=True, upload_to='profile_picture'),
        ),
    ]