# Generated by Django 3.2.8 on 2021-11-04 16:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('writer', '0010_follower'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='follower',
            name='follower_count',
        ),
        migrations.AddField(
            model_name='profile',
            name='followers',
            field=models.ManyToManyField(related_name='followers', to='writer.Follower'),
        ),
        migrations.AddField(
            model_name='profile',
            name='followers_count',
            field=models.IntegerField(default=0),
        ),
        migrations.RemoveField(
            model_name='follower',
            name='profile',
        ),
        migrations.AddField(
            model_name='follower',
            name='profile',
            field=models.OneToOneField(default=None, on_delete=django.db.models.deletion.CASCADE, to='writer.profile'),
        ),
    ]
