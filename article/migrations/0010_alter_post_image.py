# Generated by Django 3.2.8 on 2021-11-01 22:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0009_alter_post_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(default='default.jpg/', upload_to='img'),
        ),
    ]