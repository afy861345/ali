# Generated by Django 5.1.5 on 2025-01-19 15:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0020_alter_patients_visit_date_alter_photo_add_at_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='visit',
            name='file',
            field=models.FileField(null=True, upload_to='pdfs/%Y/%m/%d'),
        ),
    ]
