# Generated by Django 3.0.2 on 2020-04-03 20:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_userdata'),
    ]

    operations = [
        migrations.DeleteModel(
            name='UserData',
        ),
    ]
