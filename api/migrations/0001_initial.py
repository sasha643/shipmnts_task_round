# Generated by Django 4.0.10 on 2024-08-02 09:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ScehduleEmail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('recipient', models.EmailField(max_length=254)),
                ('subject', models.CharField(max_length=255)),
                ('body', models.TextField()),
                ('schedule_time', models.DateTimeField()),
                ('recurrence', models.CharField(choices=[('none', 'None'), ('daily', 'Daily'), ('weekly', 'Weekly'), ('monthly', 'Monthly'), ('quarterly', 'Quarterly')], default='none', max_length=10)),
                ('daily_times', models.JSONField(blank=True, null=True)),
                ('weekly_days_times', models.JSONField(blank=True, null=True)),
                ('monthly_days_times', models.JSONField(blank=True, null=True)),
                ('quarterly_days_times', models.JSONField(blank=True, null=True)),
                ('attachments', models.FileField(blank=True, null=True, upload_to='attachments/')),
            ],
        ),
    ]
