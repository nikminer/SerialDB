# Generated by Django 3.0.4 on 2020-03-31 16:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MyWatchList', '0007_auto_20200331_1845'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='length',
            field=models.PositiveSmallIntegerField(default=0),
            preserve_default=False,
        ),
    ]