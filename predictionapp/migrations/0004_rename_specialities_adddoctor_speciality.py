# Generated by Django 4.1.5 on 2023-02-02 05:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('predictionapp', '0003_adddoctor_description_adddoctor_fee_adddoctor_image_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='adddoctor',
            old_name='specialities',
            new_name='speciality',
        ),
    ]
