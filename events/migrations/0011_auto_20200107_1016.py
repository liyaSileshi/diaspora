# Generated by Django 3.0.2 on 2020-01-07 18:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0010_remove_event_slug'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='event',
            name='created',
        ),
        migrations.RemoveField(
            model_name='event',
            name='modified',
        ),
    ]