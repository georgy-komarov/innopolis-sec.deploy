# Generated by Django 2.1 on 2018-08-16 07:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('logs', '0003_auto_20180816_0710'),
    ]

    operations = [
        migrations.AlterField(
            model_name='flagattemptentry',
            name='team_sharing',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='another_team', to='teamboard.Team'),
        ),
    ]
