# Generated by Django 2.0.3 on 2018-11-15 13:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('weather', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='conditions',
            old_name='hunidity',
            new_name='humidity',
        ),
    ]
