# Generated by Django 5.1.5 on 2025-01-17 09:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0009_news'),
    ]

    operations = [
        migrations.CreateModel(
            name='Visit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(default='2025:01:17')),
                ('patient', models.ManyToManyField(related_name='visit', to='home.patients')),
            ],
        ),
    ]
