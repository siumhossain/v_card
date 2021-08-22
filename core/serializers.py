from rest_framework import serializers

from . models import CrimeInfo, User,UserProfile,ChildRecord,MedicalInfo, Visa



class RegisterSerializer(serializers.ModelSerializer):
    

    class Meta:
        model = User
        fields = ['username','email','password']
       
        def save(self):
            user = User(
                username = self.validate_data['username'],
                email=self.validated_data['email'],
                password = self.validated_data['password']
            )
            user.save()
            return user

class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = [
            'first_name',
            'last_name',
            'father_name',
            'mother_name',
            'date_of_birth',
            'email',
            'registration_date',
            'birth_certificate_number',
            'blood_group',
            'phone_number',
            'pressent_address',
            'permanent_address',
            'ssn_number'
        ]
class ProfileModifierSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = [
            'first_name',
            'last_name',
            'father_name',
            'mother_name',
            'date_of_birth',
            'email',
            'birth_certificate_number',
            'blood_group',
            'phone_number',
            'pressent_address',
            'permanent_address',
        ]

    
        
    
class UserSerializers(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username','email','ssn_number']

class CrimeSeralizersAll(serializers.ModelSerializer):
    class Meta:
        model = CrimeInfo
        fields = ['user','ssn_number','date','title_of_crime','description','red_alert']
class CrimeSeralizersCreate(serializers.ModelSerializer):
    class Meta:
        model = CrimeInfo
        fields = ['date','title_of_crime','description','red_alert']

class MedicalSeralizers(serializers.ModelSerializer):
    class Meta:
        model = MedicalInfo
        fields = ['weight','bp','oxyzen_level','suger_level','major_disease','recent_operation','briefly_describe']
class MedicalSeralizersI(serializers.ModelSerializer):
    class Meta:
        model = MedicalInfo
        fields = ['appoinment_time','weight','bp','oxyzen_level','suger_level','major_disease','recent_operation','briefly_describe']
class VisaSeralizers(serializers.ModelSerializer):
    class Meta:
        model = Visa
        fields = ['approved','description']