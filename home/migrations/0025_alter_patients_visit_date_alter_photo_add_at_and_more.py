# Generated by Django 5.1.5 on 2025-01-21 11:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0024_alter_patients_visit_date_alter_photo_add_at_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patients',
            name='visit_date',
            field=models.DateField(default='2025-01-21', null=True),
        ),
        migrations.AlterField(
            model_name='photo',
            name='add_at',
            field=models.DateField(default='2025-01-21'),
        ),
        migrations.AlterField(
            model_name='visit',
            name='date',
            field=models.DateField(default='2025-01-21'),
        ),
    ]
