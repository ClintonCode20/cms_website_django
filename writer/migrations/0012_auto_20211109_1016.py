# Generated by Django 3.2.8 on 2021-11-09 18:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('writer', '0011_auto_20211104_0926'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='followers',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='followers_count',
        ),
    ]
