# Generated by Django 3.2.6 on 2021-08-20 18:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_alter_userprofile_ssn_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='medicalinfo',
            name='appoinment_time',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
