from django.urls import path,include
from . import views 

from rest_framework.authtoken.views import obtain_auth_token


urlpatterns = [
    path('view/',views.view),
    path('profile/<str:id>/',views.user_profile),
    path('crime_profile/',views.crime_profile_all),
    path('get_individual_crime_profile/<str:ssn>/',views.get_crime_profile_individual),
    path('individual_crime_profile_create/<str:ssn>/',views.create_crime_profile_individual),
    path('update_crime_info_individual/<int:id>/',views.update_individual),
    path('delete_crime_info_individual/<int:id>/',views.update_individual),

    ########medical##########
    path('create_medical_record/<str:ssn>/',views.create_medical_recoed_individual),
    path('get_medical_record/<str:ssn>/',views.get_medical_record_individual),
    path('update_medical_record/<int:id>/',views.update_medical_record),


    ########visa#######

    path('create_visa/<str:ssn>/',views.visa_application),
  
    
    #path('user_profile/<str:ssn>/',views.get_user_profile),
    path('auth/',include('djoser.urls')),
    path('auth/',include('djoser.urls.authtoken')),


   
]