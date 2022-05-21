# Generated by Django 4.0.4 on 2022-05-07 10:38

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Venue',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120, verbose_name='Venue Name')),
                ('address', models.CharField(max_length=400, verbose_name='Venue Address')),
                ('pincode', models.CharField(max_length=10, verbose_name='Venue Post Code')),
                ('web', models.URLField(blank=True, max_length=120, verbose_name='Venue Website')),
            ],
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120, verbose_name='Event Name')),
                ('start_time', models.DateTimeField()),
                ('end_time', models.DateTimeField()),
                ('Coordinator', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
                ('venue', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='public.venue')),
            ],
        ),
        migrations.CreateModel(
            name='Attendee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120, verbose_name='Sponsor Name')),
                ('contact', models.CharField(max_length=10, verbose_name='Sponsor Number')),
                ('numOfParticipants', models.CharField(max_length=2, verbose_name='Number Of Participants')),
                ('paymentStatus', models.BooleanField(default=False, verbose_name='Aprroved')),
                ('coordinator', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='public.event')),
            ],
        ),
    ]
