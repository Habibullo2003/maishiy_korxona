# Generated by Django 4.2.2 on 2025-06-13 16:41

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='korxona',
            name='created_at',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
