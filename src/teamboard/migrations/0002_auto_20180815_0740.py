# Generated by Django 2.1 on 2018-08-15 07:40

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('teamboard', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='team',
            name='uid',
            field=models.BigIntegerField(default=5547469705514, unique=True),
        ),
        migrations.AlterField(
            model_name='team',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]