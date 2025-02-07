# Generated by Django 5.1.5 on 2025-01-19 16:54

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0022_remove_visit_file_photo_file'),
    ]

    operations = [
        migrations.AddField(
            model_name='photo',
            name='visit',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='files', to='home.visit'),
        ),
        migrations.AlterField(
            model_name='photo',
            name='patient',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='files', to='home.patients'),
        ),
    ]
