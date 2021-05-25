from django.contrib.auth import authenticate,get_user_model
from rest_framework import serializers
from .models import ValuesStored

def get_search_list(startDateTime, endDateTime,user):
    searchList = ValuesStored.objects.filter(user=user,timeStamp__range=(startDateTime, endDateTime))
    if searchList is None:
        raise serializers.ValidationError("No Search. Please try again!")
    print(searchList)
    return searchList