# Generated by Django 3.0.2 on 2020-04-04 13:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0016_auto_20200404_1307'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='avatar',
            field=models.ImageField(default='/static/defaultUser.jpeg', upload_to='images/'),
        ),
    ]