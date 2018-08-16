# Generated by Django 2.1 on 2018-08-16 07:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('teamboard', '0006_auto_20180816_0706'),
        ('logs', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='flagattemptentry',
            name='team_sharing',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='another_team', to='teamboard.Team'),
        ),
        migrations.AlterField(
            model_name='flagattemptentry',
            name='team',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='team', to='teamboard.Team'),
        ),
    ]
