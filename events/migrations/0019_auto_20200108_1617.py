# Generated by Django 3.0.2 on 2020-01-09 00:17

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('events', '0018_auto_20200107_1604'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='participants',
            field=models.ManyToManyField(blank=True, related_name='participant', to=settings.AUTH_USER_MODEL),
        ),
        migrations.DeleteModel(
            name='Participant',
        ),
    ]