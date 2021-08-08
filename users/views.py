from django.contrib.auth.models import User
from django.shortcuts import render
from . models import Profile,Team,TeamMember
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.contrib.auth.hashers import make_password
from django.db.models import Q

from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.contrib.auth import login as auth_login
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token

from django.contrib.auth.models import User

from django.db.models import Q
# Create your views here.

@api_view(['POST'])
def Registeration(request):
    data={}
    first_name=request.data.get('first_name')
    last_name=request.data.get('last_name')
    email=request.data.get('email')
    mobile_no=request.data.get('mobile_no')
    password=request.data.get('password')
    if first_name and last_name:
        if not User.objects.filter(Q(username=mobile_no)|Q(email=email)):
            user_object = User.objects.create(username=mobile_no,first_name=first_name,last_name=last_name,email=email,password=make_password(password))
            profile_obj = Profile.objects.create(user=user_object,mobile_no=mobile_no)        
            data['message'] = "Registration successful"
            data['id'] = profile_obj.id
        else:
            data['message'] = "Email or Mobile already exists"

    else:
        data['message'] = "Please send first_name, last_name, email, mobile, password mandatory fields"
    return Response(data=data)
    
def login(request):
    data = {}
    username = request.data.get('username')
    raw_password = request.data.get('password')
    print(username)
    print(raw_password )
    #import ipdb; ipdb.set_trace()
    try:
        user_object = User.objects.get(Q(username__iexact=username) | Q(email__iexact=username) | Q(profile__mobile_no=username)  )
        username = user_object.username
        print(user_object)
    except:
        pass
    
    user = authenticate(username=username, password=raw_password)
    if user is not None:
        auth_login(request, user)
        token, created = Token.objects.get_or_create(user=user)
        
        data['token'] = token.key
        data['message'] = 'login is success'
    else:
        data['error'] = 'login is failed'
    return Response(data=data)

    

