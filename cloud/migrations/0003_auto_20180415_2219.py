# Generated by Django 2.0.4 on 2018-04-16 02:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cloud', '0002_song_lyrics'),
    ]

    operations = [
        migrations.AlterField(
            model_name='word',
            name='text',
            field=models.CharField(max_length=50, unique=True),
        ),
    ]