from django.contrib import admin
from . models import  ChildRecord, CrimeInfo, MedicalInfo, Passport, User,UserProfile, Visa
# Register your models here.
class UserAdmin(admin.ModelAdmin):
    search_fields = ("ssn_number__iexact","username__icontains",)
    list_filter = ("date_joined",)
admin.site.register(User,UserAdmin)

class UserProfileAdmin(admin.ModelAdmin):
    search_fields = ("ssn_number__iexact","first_name__icontains",)
    list_filter = ("is_approved","registration_date","red_alert")

admin.site.register(UserProfile,UserProfileAdmin)

class PassportAdmin(admin.ModelAdmin):
    search_fields = ("user__ssn_number__iexact","user__first_name__icontains",)
    list_filter = ("registration_date","approved")

admin.site.register(Passport,PassportAdmin)


class CrimeAdmin(admin.ModelAdmin):
    search_fields = ("ssn_number__iexact","user__first_name__icontains")
    list_filter = ("red_alert","date","title_of_crime")


admin.site.register(CrimeInfo,CrimeAdmin)

class MedicalAdmin(admin.ModelAdmin):
    search_fields = ("ssn__iexact","first_name__icontains")
    list_filter = ("appoinment_time","major_disease")
admin.site.register(MedicalInfo,MedicalAdmin)


class ChildAdmin(admin.ModelAdmin):
    search_fields = ("birth_certificate_number__iexact","first_name__icontains")
    list_filter = ("registration_date",)
admin.site.register(ChildRecord,ChildAdmin)

class VisaAdmin(admin.ModelAdmin):
    search_fields = ("ssn_number__iexact","user__user__username__icontains")
    list_filter = ("registration_date","approved")

admin.site.register(Visa,VisaAdmin)