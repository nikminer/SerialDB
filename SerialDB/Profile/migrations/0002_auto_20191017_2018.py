# Generated by Django 2.2.4 on 2019-10-17 17:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Profile', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='sex',
            field=models.CharField(choices=[('1', 'Муж'), ('2', 'Жен')], default='1', max_length=1),
        ),
        migrations.AlterField(
            model_name='profile',
            name='photo',
            field=models.ImageField(blank=True, default='users/default.png', upload_to='users'),
        ),
    ]
