# Generated by Django 2.2.4 on 2019-09-15 18:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Main', '0030_auto_20190915_2136'),
    ]

    operations = [
        migrations.AlterField(
            model_name='season',
            name='img',
            field=models.URLField(),
        ),
    ]