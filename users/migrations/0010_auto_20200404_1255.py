# Generated by Django 3.0.2 on 2020-04-04 12:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0009_profile_avatar'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='avatar',
            field=models.ImageField(default='learning_log/media/images/defaultUser.jpeg', upload_to='images/'),
        ),
    ]
