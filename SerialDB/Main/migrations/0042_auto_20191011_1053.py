# Generated by Django 2.2.4 on 2019-10-11 07:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Main', '0041_remove_film_year'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='film',
            name='date',
        ),
        migrations.AddField(
            model_name='film',
            name='year',
            field=models.IntegerField(default=1900),
            preserve_default=False,
        ),
    ]