# Generated by Django 3.0.5 on 2020-04-11 01:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MyWatchList', '0009_movie_active'),
    ]

    operations = [
        migrations.AddField(
            model_name='season',
            name='tmdbid',
            field=models.CharField(default=0, max_length=100),
            preserve_default=False,
        ),
    ]