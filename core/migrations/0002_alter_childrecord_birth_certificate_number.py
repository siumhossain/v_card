# Generated by Django 3.2.6 on 2021-08-20 12:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='childrecord',
            name='birth_certificate_number',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]