# Generated by Django 4.1.5 on 2023-02-19 06:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('predictionapp', '0012_alter_blood_mobilenumber'),
    ]

    operations = [
        migrations.AddField(
            model_name='blood',
            name='male',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='blood',
            name='nam',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
