# Generated by Django 2.2.5 on 2020-01-01 07:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0005_remove_audio_audio'),
    ]

    operations = [
        migrations.AlterField(
            model_name='audio',
            name='image',
            field=models.ImageField(default='', upload_to='music/images'),
        ),
    ]
