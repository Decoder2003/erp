# Generated by Django 4.2.10 on 2024-02-25 06:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0005_feed_group_post_interaction_image_group_membership_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='group',
            name='image_url',
            field=models.ImageField(default='null', upload_to='groupImages/'),
        ),
        migrations.AlterField(
            model_name='image',
            name='image_url',
            field=models.ImageField(default='null', upload_to='feedImages/'),
        ),
        migrations.AlterField(
            model_name='user',
            name='user_image',
            field=models.ImageField(upload_to='userImages/'),
        ),
    ]
