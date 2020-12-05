# Generated by Django 3.1.4 on 2020-12-05 16:02

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('news', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='title',
            field=models.CharField(max_length=150, unique=True, verbose_name='заголовок'),
        ),
        migrations.AlterField(
            model_name='news',
            name='author',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL, verbose_name='автор'),
        ),
        migrations.AlterField(
            model_name='news',
            name='category',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.PROTECT, to='news.category', verbose_name='категория'),
        ),
    ]