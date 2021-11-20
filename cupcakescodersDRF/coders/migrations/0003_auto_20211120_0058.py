# Generated by Django 3.2.5 on 2021-11-20 00:58

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('coders', '0002_auto_20211116_0709'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='coders',
            name='email',
        ),
        migrations.RemoveField(
            model_name='coders',
            name='first_name',
        ),
        migrations.RemoveField(
            model_name='coders',
            name='last_name',
        ),
        migrations.AlterField(
            model_name='coders',
            name='student_ID',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='student_ID_coders', to=settings.AUTH_USER_MODEL),
        ),
    ]