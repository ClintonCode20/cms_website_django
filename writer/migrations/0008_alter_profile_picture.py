# Generated by Django 3.2.8 on 2021-11-01 22:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('writer', '0007_alter_profile_picture'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='picture',
            field=models.ImageField(blank=True, default='/user-default.png', null=True, upload_to='img'),
        ),
    ]
