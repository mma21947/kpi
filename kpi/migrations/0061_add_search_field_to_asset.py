# Generated by Django 4.2.15 on 2024-12-11 23:12

from django.db import migrations
from django.db import models


class Migration(migrations.Migration):

    dependencies = [
        ('kpi', '0060_rename_exporttask_submissionexporttask_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='asset',
            name='search_field',
            field=models.JSONField(default=dict),
        ),
    ]
