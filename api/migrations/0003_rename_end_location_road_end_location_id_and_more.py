# Generated by Django 4.0.10 on 2024-08-02 10:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_location_road_trafficupdate_delete_scehduleemail'),
    ]

    operations = [
        migrations.RenameField(
            model_name='road',
            old_name='end_location',
            new_name='end_location_id',
        ),
        migrations.RenameField(
            model_name='road',
            old_name='start_location',
            new_name='start_location_id',
        ),
    ]
