# Generated by Django 2.2.5 on 2020-01-03 17:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0012_detail_provideinnerhtml'),
    ]

    operations = [
        migrations.AddField(
            model_name='detail',
            name='number',
            field=models.CharField(default=0, max_length=40),
        ),
    ]