# Generated by Django 2.1 on 2018-08-25 20:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teamboard', '0006_auto_20180824_1225'),
    ]

    operations = [
        migrations.AlterField(
            model_name='team',
            name='invite',
            field=models.CharField(max_length=50, unique=True),
        ),
        migrations.AlterField(
            model_name='team',
            name='solved_tasks',
            field=models.ManyToManyField(blank=True, to='adminboard.Task'),
        ),
    ]
