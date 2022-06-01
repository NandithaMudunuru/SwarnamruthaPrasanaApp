# Generated by Django 4.0.4 on 2022-06-01 16:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('public', '0002_alter_event_end_time_alter_event_start_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='end_time',
            field=models.DateTimeField(default='2022-06-01 19:37'),
        ),
        migrations.AlterField(
            model_name='event',
            name='start_time',
            field=models.DateTimeField(default='2022-06-01 18:37'),
        ),
        migrations.AlterField(
            model_name='event',
            name='venue',
            field=models.ForeignKey(blank=True, limit_choices_to={'is_superuser': False}, null=True, on_delete=django.db.models.deletion.PROTECT, to='public.venue'),
        ),
    ]