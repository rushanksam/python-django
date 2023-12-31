# Generated by Django 4.2.2 on 2023-06-23 07:09

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DeviceConfig',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('device_name', models.CharField(max_length=150, verbose_name='deviceconfig')),
                ('created_dt', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_dt', models.DateTimeField(auto_now_add=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Milestone',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('milestone_name', models.CharField(max_length=150, verbose_name='milestone')),
                ('created_dt', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_dt', models.DateTimeField(auto_now_add=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='POD',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pod_name', models.CharField(max_length=150, verbose_name='pod')),
                ('created_dt', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_dt', models.DateTimeField(auto_now_add=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Priority',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('priority_name', models.CharField(max_length=10, verbose_name='priority')),
                ('created_dt', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_dt', models.DateTimeField(auto_now_add=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Upload',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(upload_to='uploads/', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['csv', 'xml', 'xls'])])),
                ('created_dt', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_dt', models.DateTimeField(auto_now_add=True, null=True)),
                ('device', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='device_up', to='testcases.deviceconfig')),
                ('milestone', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='milestone_up', to='testcases.milestone')),
                ('pod', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='pod_up', to='testcases.pod')),
                ('priority', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='priority_up', to='testcases.priority')),
            ],
        ),
        migrations.CreateModel(
            name='TestCase',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('passed', models.PositiveIntegerField(blank=True, default=0)),
                ('passpercentage', models.PositiveIntegerField(blank=True, default=0)),
                ('failed', models.PositiveIntegerField(blank=True, default=0)),
                ('failpercentage', models.PositiveIntegerField(blank=True, default=0)),
                ('blocked', models.PositiveIntegerField(blank=True, default=0)),
                ('blockpercentage', models.PositiveIntegerField(blank=True, default=0)),
                ('skipped', models.PositiveIntegerField(blank=True, default=0)),
                ('skippercentage', models.PositiveIntegerField(blank=True, default=0)),
                ('untested', models.PositiveIntegerField(blank=True, default=0)),
                ('untestpercentage', models.PositiveIntegerField(blank=True, default=0)),
                ('bugs', models.TextField(blank=True, max_length=1000, null=True)),
                ('total', models.PositiveIntegerField(blank=True, default=0)),
                ('remarks', models.CharField(blank=True, max_length=1000, null=True)),
                ('created_dt', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_dt', models.DateTimeField(auto_now_add=True, null=True)),
                ('device', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='device_tc', to='testcases.deviceconfig')),
                ('milestone', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='milestone_tc', to='testcases.milestone')),
                ('pod', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='pod_tc', to='testcases.pod')),
                ('priority', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='priority_tc', to='testcases.priority')),
            ],
            options={
                'verbose_name_plural': 'DashBoard',
            },
        ),
    ]
