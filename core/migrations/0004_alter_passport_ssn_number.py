# Generated by Django 3.2.6 on 2021-08-20 16:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_auto_20210820_1605'),
    ]

    operations = [
        migrations.AlterField(
            model_name='passport',
            name='ssn_number',
            field=models.CharField(blank=True, editable=False, max_length=100),
        ),
    ]
