# Generated by Django 3.0.4 on 2020-04-07 19:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Profile', '0011_auto_20200403_1340'),
    ]

    operations = [
        migrations.CreateModel(
            name='Follower',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, db_index=True)),
                ('follow_from', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='rel_from_set', to='Profile.Profile')),
                ('follow_to', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='rel_to_set', to='Profile.Profile')),
            ],
            options={
                'ordering': ('-created',),
            },
        ),
        migrations.AddField(
            model_name='profile',
            name='fillowing',
            field=models.ManyToManyField(related_name='followers', through='Profile.Follower', to='Profile.Profile'),
        ),
    ]
