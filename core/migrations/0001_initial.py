# Generated by Django 3.2.6 on 2021-08-20 11:44

from django.conf import settings
import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import django_cryptography.fields
import phonenumber_field.modelfields
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('ssn_number', models.CharField(blank=True, default='', max_length=100)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='ChildRecord',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('birth_certificate_number', models.CharField(max_length=100)),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('father_name', models.CharField(blank=True, max_length=100)),
                ('mother_name', models.CharField(blank=True, max_length=100)),
                ('date_of_birth', models.DateTimeField(blank=True, null=True)),
                ('blood_group', models.CharField(blank=True, max_length=3)),
                ('registration_date', models.DateTimeField(auto_now_add=True)),
                ('citizenship_by_birth', models.BooleanField(default=False)),
                ('pressent_address', django_cryptography.fields.encrypt(models.TextField(blank=True))),
                ('permanent_address', django_cryptography.fields.encrypt(models.TextField(blank=True))),
            ],
        ),
        migrations.CreateModel(
            name='CrimeInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ssn_number', models.CharField(max_length=100)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('title_of_crime', models.CharField(max_length=300)),
                ('description', models.TextField(blank=True)),
                ('red_alert', models.BooleanField(default=False)),
            ],
            options={
                'ordering': ['-date'],
            },
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(blank=True, max_length=50)),
                ('last_name', models.CharField(blank=True, max_length=50)),
                ('father_name', models.CharField(blank=True, max_length=100)),
                ('mother_name', models.CharField(blank=True, max_length=100)),
                ('date_of_birth', models.DateTimeField(blank=True, null=True)),
                ('email', django_cryptography.fields.encrypt(models.EmailField(blank=True, max_length=100))),
                ('blood_group', models.CharField(blank=True, max_length=3)),
                ('registration_date', models.DateTimeField(auto_now_add=True)),
                ('citizenship_by_birth', models.BooleanField(default=False)),
                ('birth_certificate_number', django_cryptography.fields.encrypt(models.CharField(blank=True, max_length=100))),
                ('phone_number', django_cryptography.fields.encrypt(phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=128, null=True, region=None))),
                ('pressent_address', django_cryptography.fields.encrypt(models.TextField(blank=True))),
                ('permanent_address', django_cryptography.fields.encrypt(models.TextField(blank=True))),
                ('ssn_number', django_cryptography.fields.encrypt(models.CharField(blank=True, default='', editable=False, max_length=100))),
                ('is_approved', models.BooleanField(default=False)),
                ('red_alert', models.BooleanField(default=False)),
                ('can_update', models.BooleanField(default=False)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Passport',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('father_name', models.CharField(blank=True, max_length=100)),
                ('mother_name', models.CharField(blank=True, max_length=100)),
                ('date_of_birth', models.DateTimeField(blank=True, null=True)),
                ('email', django_cryptography.fields.encrypt(models.EmailField(max_length=100))),
                ('blood_group', models.CharField(blank=True, max_length=3)),
                ('registration_date', models.DateTimeField(auto_now_add=True)),
                ('citizenship_by_birth', models.BooleanField(default=False)),
                ('birth_certificate_number', django_cryptography.fields.encrypt(models.CharField(blank=True, max_length=100))),
                ('phone_number', django_cryptography.fields.encrypt(phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=128, null=True, region=None))),
                ('pressent_address', django_cryptography.fields.encrypt(models.TextField(blank=True))),
                ('permanent_address', django_cryptography.fields.encrypt(models.TextField(blank=True))),
                ('ssn_number', django_cryptography.fields.encrypt(models.CharField(blank=True, editable=False, max_length=100))),
                ('emergency_contact_info', models.TextField(blank=True)),
                ('emergency_contact', django_cryptography.fields.encrypt(phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=128, region=None))),
                ('approved', models.BooleanField(default=False)),
                ('police_verification_record', models.OneToOneField(default='', on_delete=django.db.models.deletion.CASCADE, to='core.crimeinfo')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='core.userprofile')),
            ],
        ),
        migrations.CreateModel(
            name='MedicalInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('appoinment_time', models.DateTimeField(auto_now_add=True)),
                ('ssn', models.CharField(max_length=100)),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('weight', models.CharField(max_length=100)),
                ('bp', models.CharField(max_length=100)),
                ('oxyzen_level', models.CharField(blank=True, max_length=100)),
                ('suger_level', models.CharField(blank=True, max_length=100)),
                ('major_disease', models.CharField(blank=True, max_length=100)),
                ('recent_operation', models.CharField(blank=True, max_length=100)),
                ('briefly_describe', models.TextField(blank=True)),
                ('user', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='core.userprofile')),
            ],
            options={
                'ordering': ['-appoinment_time'],
            },
        ),
        migrations.AddField(
            model_name='crimeinfo',
            name='user',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='core.userprofile'),
        ),
    ]
