
from django.shortcuts import render
from rest_framework import status
from django.views.decorators.csrf import csrf_exempt

from rest_framework.decorators import api_view,permission_classes
from rest_framework.response import Response
from .models import UserProfile,ChildRecord,CrimeInfo,MedicalInfo, VisaCenter

from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated
from core.serializers import MedicalSeralizersI, ProfileModifierSerializer, RegisterSerializer,UserProfileSerializer,CrimeSeralizersAll,CrimeSeralizersCreate,MedicalSeralizers, VisaSeralizers
# Create your views here.



@api_view(['GET'])
@permission_classes([IsAuthenticated])
def view(request):
   return Response({"hello":"hello"})
@api_view(['POST'])
def register(request):
   if request.method == 'POST':
      serializer = RegisterSerializer(data=request.data)
      data = {}
      if serializer.is_valid():
         user = serializer.save()
         data['response'] = "success"
         data['email'] = user.email
         token = Token.objects.get(user=user).key
         
         data['token'] = token
      else:
         data = serializer.errors
      return Response(data)



########Crime unit###########
@api_view(['GET','PUT'])
@permission_classes([IsAuthenticated])
def user_profile(request,id):
   user_profile=UserProfile.objects.get(user_id=id)
   
   if request.user.id != user_profile.user_id:
      return Response(status=status.HTTP_403_FORBIDDEN)
   else:
      approved = user_profile.is_approved
      if request.method == 'GET':
         serializer = UserProfileSerializer(user_profile)
         return Response(serializer.data)
      if approved:
         return Response({'Message':'You can not edit aftere approve,you have to take permission.Please contact with us'})
      elif request.method == 'PUT':
         data = request.data
         serializer = ProfileModifierSerializer(user_profile,data=request.data)
         if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
         return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
      

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def crime_profile_all(request):
   if request.method == 'GET':
      crime_list = CrimeInfo.objects.all()
      serializer = CrimeSeralizersAll(crime_list,many=True)
      return Response(serializer.data)
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_crime_profile_individual(request,ssn):
   try:
      crime_list = CrimeInfo.objects.filter(ssn_number__exact=ssn)
   except CrimeInfo.DoesNotExist:
      return Response({"error":"not found"})

   if request.method == 'GET':
      
      serializer = CrimeSeralizersAll(crime_list,many=True)
      return Response(serializer.data)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create_crime_profile_individual(request,ssn):
   try:
      user = UserProfile.objects.get(ssn_number=ssn)
   except UserProfile.DoesNotExist:
      return Response({"error":"not found"})
   crime_record = CrimeInfo(ssn_number=ssn,user_id=user.id)
   if request.method == 'POST':
      serializer = CrimeSeralizersCreate(crime_record,data=request.data)
      if serializer.is_valid():
         serializer.save()
         return Response(serializer.data,status=status.HTTP_201_CREATED)
      return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT','DELETE'])
@permission_classes([IsAuthenticated])
def update_individual(request,id):
   try:
      crime_record = CrimeInfo.objects.get(id=id)
   except CrimeInfo.DoesNotExist:
      return Response({"error":"not found"})
   if request.method == 'PUT':
      serializer = CrimeSeralizersCreate(crime_record,data=request.data)
      if serializer.is_valid():
         serializer.save()
         return Response(serializer.data,status=status.HTTP_201_CREATED)
      return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
   if request.method == 'DELETE':
      operation = crime_record.delete()
      data = {}

      if operation:
         data['success'] = 'deleted'
      else:
         data['failure'] = 'failed'

      return Response(data=data)

########Crime unit###########


########Medical########
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create_medical_recoed_individual(request,ssn):
   try:
      user = UserProfile.objects.get(ssn_number=ssn)
   except UserProfile.DoesNotExist:
      return Response({"error":"not found"})
   medical_record = MedicalInfo(ssn=ssn,user_id=user.id,first_name=user.first_name,last_name=user.last_name)
   if request.method == 'POST':
      serializer = MedicalSeralizers(medical_record,data=request.data)
      if serializer.is_valid():
         serializer.save()
         return Response(serializer.data,status=status.HTTP_201_CREATED)
      return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_medical_record_individual(request,ssn):
   try:
      medical = MedicalInfo.objects.filter(ssn__exact=ssn)
   except MedicalInfo.DoesNotExist:
      return Response({"error":"not found"})

   if request.method == 'GET':
      
      serializer = MedicalSeralizersI(medical,many=True)
      return Response(serializer.data)

@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def update_medical_record(request,id):
   try:
      medical_record = MedicalInfo.objects.get(id=id)
   except CrimeInfo.DoesNotExist:
      return Response({"error":"not found"})
   if request.method == 'PUT':
      serializer = MedicalSeralizers(medical_record,data=request.data)
      if serializer.is_valid():
         serializer.save()
         return Response(serializer.data,status=status.HTTP_201_CREATED)
      return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def visa_application(request,ssn):
   try:
      user = UserProfile.objects.get(ssn_number=ssn)
   except UserProfile.DoesNotExist:
      return Response({"error":"not found"})
   red_alert = user.red_alert
   print(red_alert)
   if red_alert:
      return Response({'alert':'this guy is criminal-call 999 Asap!!!'})
   else:
      visa_record = VisaCenter(ssn_number=user.ssn_number,user_id=user.id)
      if request.method == 'POST':
         serializer = VisaSeralizers(visa_record,data=request.data)
         if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
         return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
