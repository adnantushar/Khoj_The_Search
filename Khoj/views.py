from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login,get_user_model,logout
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ImproperlyConfigured
from rest_framework import viewsets, status
from rest_framework.authentication import SessionAuthentication, TokenAuthentication
from rest_framework.decorators import action
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response

from . import serializers
from .models import ValuesStored
from .utils import get_search_list
import requests
import datetime
# Create your views here.

def SignUp(request):
    context = {}
    if request.method == 'POST':
        firstname = request.POST['Username1']
        lastname = request.POST['Username2']
        email = request.POST['email']
        password = request.POST['password']
        print(firstname,lastname,email,password)
        url = 'http://127.0.0.1:8000/api/auth/register'
        data = {'email': email,'password': password,'first_name': firstname,'last_name': 'lastname'}
        r = requests.post(url=url, data=data) #user register api request
        result = r.json()
        if r.ok:
            '''print(result['id'])
            url = 'http://127.0.0.1:8000/api/auth/login'
            data = {'email': email, 'password': password} #user login api request
            l = requests.post(url=url, data=data)
            if l.ok:
                return redirect("/")'''
            user = authenticate(email=email, password=password)
            if user is not None and user.is_active:
                login(request, user)
                return redirect("/")
        else:
            print(result,result['email'][0])
            context = {'result':result,'flag':1 }
            render(request,'signup.html',context)

    return  render(request,'signup.html',context)

def LogIn(request):
    msg = ''
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        print(email, password)
        ''''
        url = 'http://127.0.0.1:8000/api/auth/login'
        data = {'email': email, 'password': password}
        l = requests.post(url=url, data=data)   #calling login api

        if l.ok:'''
        user = authenticate(email=email, password=password)
        if user is not None and user.is_active:
            login(request, user)
            return redirect("/")
        else:
            msg = "InValid Credentials"
            render(request,'login.html',{'msg':msg})

    return  render(request,'login.html',{'msg':msg})


def LogOut(request):
    logout(request)
    return redirect('/login')

@login_required(login_url="/login/")
def Home(request):
    context = {}
    if request.method == 'POST':
        inputValues = request.POST['InputValues']
        searchValue = int(request.POST['SearchNumber'])
        #print(inputValues, searchValue)
        values = str(inputValues.strip("")).split(',') #removing "," and creating lists
        integer_map = map(int, values) #Converting string to integer of list each value
        values = list(integer_map) #Converting map to list
        values.sort(reverse=True) # Sorting in descending order
        #print(values)
        if searchValue in values:
            khoj = True
        else:
            khoj = False
        #print(khoj)
        obj = ValuesStored.objects.create(user=request.user,inputValues=values)
        obj.save()
        context = {'values':values, 'searchValue':searchValue,'flag':True,'khoj':khoj}
        return render(request, 'home.html',context)

    return render(request, 'home.html',context)

@login_required(login_url="/login/")
def SearchList(request):
    if request.method == 'POST':
        startDateTime = request.POST['startTime']
        endDateTime = request.POST['endtime']
        startDateTime = datetime.datetime.strptime(startDateTime, '%Y-%m-%dT%H:%M')
        endDateTime = datetime.datetime.strptime(endDateTime, '%Y-%m-%dT%H:%M')
        #print(startDateTime,endDateTime,datetime.datetime.now())
        #Query For User Search List Form StartTime To End TIme
        data = ValuesStored.objects.filter(user=request.user,timeStamp__range=(startDateTime, endDateTime))
        #print(data)
        '''
        d={'startDateTime':'2021-05-20 17:59:00','endDateTime':'2021-05-25 18:00:00'}
        url = 'http://127.0.0.1:8000/api/searchlist'
        headers = {'Authorization': 'Token 2e932e2db63a5d79e69625ea6b2b008a12843b1f'}
        r = requests.post(url,data=d, headers=headers)
        print(r)'''
        context = {'data':data,'flag':True,'start':startDateTime,'end':endDateTime}
        return render(request, 'searchlist.html', context)
    context = {"flag":False}
    return render(request, 'searchlist.html',context)

class SearchListViewSet(viewsets.GenericViewSet):
    permission_classes = [AllowAny, ]
    authentication_classes = (
        TokenAuthentication,
    )
    serializer_class = serializers.EmptySerializer
    serializer_classes = {
        'searchlist': serializers.SearchFormSerializer,
    }

    @action(methods=['POST', ], detail=False, permission_classes = [IsAuthenticated, ] )
    def searchlist(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        Lists = get_search_list(**serializer.validated_data,user=request.user)
        data = serializers.SearchListSerializer(Lists).data
        return Response(data=data, status=status.HTTP_200_OK)

    def get_serializer_class(self):
        if not isinstance(self.serializer_classes, dict):
            raise ImproperlyConfigured("serializer_classes should be a dict mapping.")

        if self.action in self.serializer_classes.keys():
            return self.serializer_classes[self.action]
        return super().get_serializer_class()
