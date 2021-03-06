# Generated by Django 4.0.2 on 2022-03-01 17:42

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('sweatygames', '0002_team'),
    ]

    operations = [
        migrations.AddField(
            model_name='team',
            name='gametype',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='sweatygames.season'),
        ),
        migrations.AddField(
            model_name='team',
            name='leader',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]
