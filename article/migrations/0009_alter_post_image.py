# Generated by Django 3.2.8 on 2021-11-01 22:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0008_alter_post_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(default='img/default.jpg', upload_to='img'),
        ),
    ]