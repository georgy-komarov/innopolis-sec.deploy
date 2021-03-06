# Generated by Django 2.1 on 2018-08-22 08:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('teamboard', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='LogEntry',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time', models.DateTimeField(auto_now_add=True)),
                ('ip', models.GenericIPAddressField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='AdminPanelEntry',
            fields=[
                ('logentry_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='logs.LogEntry')),
                ('valid', models.BooleanField(default=False)),
            ],
            bases=('logs.logentry',),
        ),
        migrations.CreateModel(
            name='AuditEntry',
            fields=[
                ('logentry_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='logs.LogEntry')),
                ('action', models.CharField(max_length=64)),
                ('username', models.CharField(max_length=256, null=True)),
            ],
            bases=('logs.logentry',),
        ),
        migrations.CreateModel(
            name='FlagAttemptEntry',
            fields=[
                ('logentry_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='logs.LogEntry')),
                ('flag', models.CharField(max_length=100)),
                ('valid', models.BooleanField(default=False)),
                ('sharing', models.BooleanField(default=False)),
                ('team', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='team', to='teamboard.Team')),
                ('team_sharing', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='another_team', to='teamboard.Team')),
            ],
            bases=('logs.logentry',),
        ),
    ]
