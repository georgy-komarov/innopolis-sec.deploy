# Generated by Django 2.1 on 2018-08-24 12:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teamboard', '0005_auto_20180824_1058'),
    ]

    operations = [
        migrations.AlterField(
            model_name='team',
            name='solved_tasks',
            field=models.ManyToManyField(blank=True, null=True, to='adminboard.Task'),
        ),
    ]
