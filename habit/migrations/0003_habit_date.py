# Generated by Django 5.0.3 on 2024-04-07 06:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('habit', '0002_alter_habit_time'),
    ]

    operations = [
        migrations.AddField(
            model_name='habit',
            name='date',
            field=models.DateField(blank=True, null=True, verbose_name='дата'),
        ),
    ]
