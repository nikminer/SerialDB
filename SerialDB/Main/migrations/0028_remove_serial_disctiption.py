# Generated by Django 2.2 on 2019-08-12 03:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Main', '0027_auto_20190807_0439'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='serial',
            name='disctiption',
        ),
    ]
