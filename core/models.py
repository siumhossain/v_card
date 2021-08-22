from django.db import models
from django.contrib.auth.models import AbstractUser
import uuid
from django_cryptography.fields import encrypt
from django.db.models.signals import post_save
from faker import Faker 
from phonenumber_field.modelfields import PhoneNumberField
from django.conf import settings
from django.dispatch import receiver
from rest_framework.authtoken.models import Token


# Create your models here.
fake = Faker()
class User(AbstractUser):
    id =  models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    ssn_number = models.CharField(max_length=100,default='', blank=True)

    def save(self,*args,**kwargs):
        self.ssn_number = fake.ssn()
        super().save(*args, **kwargs)
    def __str__(self):
        return f'{self.username}'

    

def post_user(sender,instance,created,**kwargs):
    if created:
        user = User.objects.get(id=instance.id)
        UserProfile.objects.create(
            user = user,
            first_name = user.first_name,
            last_name = user.last_name,
            email = user.email,
            registration_date = user.date_joined,
            ssn_number = user.ssn_number

        )
post_save.connect(post_user,sender=User)




class Passport(models.Model):
    user = models.OneToOneField("UserProfile",on_delete=models.CASCADE)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    father_name = models.CharField(max_length=100,blank=True)
    mother_name = models.CharField(max_length=100,blank=True)
    date_of_birth = models.DateTimeField(blank=True,null=True)
    email = encrypt(models.EmailField(max_length=100)) 
    blood_group = models.CharField(max_length=3,blank=True)
    registration_date = models.DateTimeField(auto_now_add=True)
    citizenship_by_birth = models.BooleanField(default=False)
    birth_certificate_number = encrypt(models.CharField(max_length=100,blank=True)) 
    phone_number = encrypt(PhoneNumberField(blank=True,null=True)) 
    pressent_address = encrypt(models.TextField(blank=True))
    permanent_address = encrypt(models.TextField(blank=True))
    ssn_number = models.CharField(max_length=100,blank=True,editable = False)
    emergency_contact_info = models.TextField(blank=True)
    emergency_contact = encrypt(PhoneNumberField(blank=True)) 
    approved = models.BooleanField(default=False)
    police_verification_record = models.OneToOneField("CrimeInfo",on_delete=models.CASCADE,default='')

    def __str__(self):
        return f'{self.ssn_number} | {self.first_name} {self.last_name}'

class CrimeInfo(models.Model):
    user = models.ForeignKey("UserProfile",on_delete=models.CASCADE,default='')
    ssn_number = models.CharField(max_length=100,blank=True)
    date = models.DateTimeField(auto_now_add=True,null=True)
    title_of_crime = models.CharField(max_length=300,blank=True)
    description = models.TextField(blank=True)
    red_alert = models.BooleanField(default=False)
    def __str__(self):
        return f'{self.ssn_number}'
    class Meta:
        ordering = ['-date']


class MedicalInfo(models.Model):
    user = models.ForeignKey("UserProfile",on_delete=models.CASCADE,default='')
    appoinment_time = models.DateTimeField(auto_now_add=True,null=True)
    ssn = models.CharField(max_length=100)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    weight = models.CharField(max_length=100,blank=True)
    bp = models.CharField(max_length=100,blank=True)
    oxyzen_level = models.CharField(max_length=100, blank=True)
    suger_level = models.CharField(max_length=100,blank=True)
    major_disease = models.CharField(max_length=100,blank=True)
    recent_operation = models.CharField(max_length=100,blank=True)
    briefly_describe = models.TextField(blank=True)

    def __str__(self):
        return f'{self.ssn_number} | {self.first_name} {self.last_name}'

    class Meta:
        ordering = ['-appoinment_time']


class ChildRecord(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    birth_certificate_number = models.CharField(max_length=100, blank=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    father_name = models.CharField(max_length=100,blank=True)
    mother_name = models.CharField(max_length=100,blank=True)
    date_of_birth = models.DateTimeField(blank=True,null=True)
    blood_group = models.CharField(max_length=3,blank=True)
    registration_date = models.DateTimeField(auto_now_add=True)
    citizenship_by_birth = models.BooleanField(default=False)
    pressent_address = encrypt(models.TextField(blank=True))
    permanent_address = encrypt(models.TextField(blank=True))

    def __str__(self):
        return f'{self.birth_certificate_number} | {self.first_name} {self.last_name}'
    def save(self,*args,**kwargs):
        self.birth_certificate_number = fake.ssn()
        super().save(*args, **kwargs)


class UserProfile(models.Model):
    BLOOD_GROUP = (
        ('A+','A+'),
        ('B+','B+'),
        ('O+','O+'),
        ('AB+','AB+'),
        ('A-','A-'),
        ('B-','B-'),
        ('O-','O-'),
        ('AB-','AB-'),
    )
    user = models.OneToOneField("User",on_delete=models.CASCADE)
    first_name = models.CharField(max_length=50,blank=True)
    last_name = models.CharField(max_length=50,blank=True)
    father_name = models.CharField(max_length=100,blank=True)
    mother_name = models.CharField(max_length=100,blank=True)
    date_of_birth = models.DateTimeField(blank=True,null=True)
    email = encrypt(models.EmailField(max_length=100, blank=True)) 
    blood_group = models.CharField(max_length=3,blank=True)
    registration_date = models.DateTimeField(auto_now_add=True)
    citizenship_by_birth = models.BooleanField(default=False)
    birth_certificate_number = encrypt(models.CharField(max_length=100,blank=True)) 
    phone_number = encrypt(PhoneNumberField(blank=True,null=True)) 
    pressent_address = encrypt(models.TextField(blank=True))
    permanent_address = encrypt(models.TextField(blank=True))
    ssn_number = models.CharField(max_length=100,blank=True,editable = False,default='')
    is_approved = models.BooleanField(default=False)
    red_alert = models.BooleanField(default=False)
    can_update = models.BooleanField(default=False)
    def __str__(self):
        return f'{self.user.username} | {self.user.ssn_number}'




class Visa(models.Model):
    user = models.ForeignKey(UserProfile,on_delete=models.CASCADE,default='')
    ssn_number = models.CharField(max_length=100,blank=True)
    approved = models.BooleanField(default=False)
    description = models.TextField(blank=True)
    registration_date = models.DateTimeField(auto_now_add=True,null=True)

    def __str__(self):
        return self.user