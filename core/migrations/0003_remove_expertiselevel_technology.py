# Generated by Django 3.2.16 on 2022-11-21 14:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20221121_2025'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='expertiselevel',
            name='technology',
        ),
    ]
