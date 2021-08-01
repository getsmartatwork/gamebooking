from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.contrib.auth import login as auth_login
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token

from django.contrib.auth.models import User

from django.db.models import Q
# Create your views here.

@api_view(['POST'])
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

    

