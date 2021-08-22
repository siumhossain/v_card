# Generated by Django 3.2.6 on 2021-08-21 06:19

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_auto_20210820_1854'),
    ]

    operations = [
        migrations.CreateModel(
            name='VisaCenter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ssn_number', models.CharField(max_length=100)),
                ('approved', models.BooleanField(default=False)),
                ('description', models.TextField(blank=True)),
                ('user', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
