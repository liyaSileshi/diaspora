# Generated by Django 3.0.2 on 2020-01-07 18:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0012_auto_20200107_1020'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='event',
            name='author',
        ),
    ]
