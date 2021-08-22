from django.contrib import admin
from . models import  ChildRecord, CrimeInfo, MedicalInfo, Passport, User,UserProfile, VisaCenter
# Register your models here.
admin.site.register(User)
admin.site.register(UserProfile)
admin.site.register(Passport)
admin.site.register(CrimeInfo)
admin.site.register(MedicalInfo)
admin.site.register(ChildRecord)
admin.site.register(VisaCenter)