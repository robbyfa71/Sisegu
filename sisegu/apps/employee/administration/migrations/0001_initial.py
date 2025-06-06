# Generated by Django 5.1.9 on 2025-05-27 15:09

import django.db.models.deletion
import django.utils.timezone
import phonenumber_field.modelfields
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Branches',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=70)),
                ('address', models.TextField()),
                ('phone_number', phonenumber_field.modelfields.PhoneNumberField(max_length=128, region='ID')),
                ('status', models.BooleanField(default=False)),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('created_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Branches',
            },
        ),
        migrations.CreateModel(
            name='IncomingMail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mail_type', models.IntegerField(choices=[(1, 'Undangan'), (2, 'Surat Keputusan'), (3, 'Surat Perintah'), (4, 'Surat Permohonan'), (5, 'Surat Pemberitahuan'), (6, 'Proposal'), (7, 'Surat Peminjaman')], default=1)),
                ('mail_number', models.CharField(blank=True, max_length=50)),
                ('mail_purpose', models.TextField(blank=True)),
                ('sender', models.CharField(max_length=150)),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('created_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Incoming Mails',
            },
        ),
        migrations.CreateModel(
            name='Members',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('birth_date', models.DateField()),
                ('tier', models.IntegerField(choices=[(1, 'Siswa Melati 1'), (2, 'Siswa Melati 2'), (3, 'Siswa Melati 3'), (4, 'Siswa Melati 4'), (5, 'Kader Dasar'), (6, 'Kader Muda'), (7, 'Kader Madya'), (8, 'Kader Kepala'), (9, 'Kader Utama'), (10, 'Pendekar Muda'), (11, 'Pendekar Madya'), (12, 'Pendekar Kepala'), (13, 'Pendekar Utama'), (14, 'Pendekar Besar')], default=1)),
                ('years_of_joining', models.CharField(max_length=4)),
                ('branch', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='administration.branches')),
            ],
            options={
                'verbose_name': 'Member',
            },
        ),
        migrations.CreateModel(
            name='OutgoingMail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mail_type', models.IntegerField(choices=[(1, 'Undangan'), (2, 'Surat Keputusan'), (3, 'Surat Perintah'), (4, 'Surat Permohonan'), (5, 'Surat Pemberitahuan'), (6, 'Proposal'), (7, 'Surat Peminjaman')], default=1)),
                ('mail_number', models.CharField(blank=True, max_length=50)),
                ('subject', models.CharField(max_length=150)),
                ('recipient', models.CharField(blank=True, max_length=150)),
                ('event_name', models.CharField(max_length=150)),
                ('event_location', models.CharField(blank=True, max_length=150)),
                ('event_Date', models.DateTimeField(blank=True, null=True)),
                ('signed_by', models.CharField(max_length=80)),
                ('signed_date', models.DateField()),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('created_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Outgoing Mails',
            },
        ),
    ]
