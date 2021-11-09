# Generated by Django 3.2.8 on 2021-11-01 21:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('writer', '0002_profile_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='name',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='picture',
            field=models.ImageField(blank=True, null=True, upload_to='img'),
        ),
    ]
