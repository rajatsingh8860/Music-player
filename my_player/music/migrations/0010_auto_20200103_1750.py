# Generated by Django 2.2.5 on 2020-01-03 12:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0009_auto_20200103_1740'),
    ]

    operations = [
        migrations.AlterField(
            model_name='detail',
            name='text',
            field=models.CharField(max_length=10000),
        ),
    ]
