# Generated by Django 3.1.4 on 2020-12-13 19:32

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('account', '0004_profile_job'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='date_of_birth',
            field=models.DateField(blank=True, null=True, verbose_name='дата рождения'),
        ),
    ]
