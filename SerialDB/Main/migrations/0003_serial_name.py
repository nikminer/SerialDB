# Generated by Django 2.2 on 2019-07-23 23:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Main', '0002_remove_serial_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='serial',
            name='name',
            field=models.CharField(default='', max_length=200),
            preserve_default=False,
        ),
    ]
