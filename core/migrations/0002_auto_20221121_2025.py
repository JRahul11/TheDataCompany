# Generated by Django 3.2.16 on 2022-11-21 14:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name_plural': 'Categories'},
        ),
        migrations.AlterModelOptions(
            name='expertiselevel',
            options={'verbose_name_plural': 'Expertise Level'},
        ),
        migrations.AlterModelOptions(
            name='technology',
            options={'verbose_name_plural': 'Technologies'},
        ),
        migrations.AlterModelOptions(
            name='usertechstack',
            options={'verbose_name_plural': 'Users Tech Stack'},
        ),
        migrations.AlterField(
            model_name='expertiselevel',
            name='level',
            field=models.CharField(max_length=30),
        ),
    ]