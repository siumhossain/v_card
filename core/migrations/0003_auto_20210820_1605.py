# Generated by Django 3.2.6 on 2021-08-20 16:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_alter_childrecord_birth_certificate_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='crimeinfo',
            name='date',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AlterField(
            model_name='crimeinfo',
            name='ssn_number',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='crimeinfo',
            name='title_of_crime',
            field=models.CharField(blank=True, max_length=300),
        ),
    ]
