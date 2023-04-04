from django.shortcuts import render
from django.db.models import Sum
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.core.exceptions import ObjectDoesNotExist
from django.utils.crypto import get_random_string
from rest_framework.decorators import authentication_classes, permission_classes
from datetime import datetime, date, timedelta
from rest_framework.status import (
    HTTP_400_BAD_REQUEST,
    HTTP_404_NOT_FOUND,
    HTTP_200_OK
)
from .models import *
from .serializers import *
import random
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken
from django.db.models import Q

from django.db.models import F, Value, Func

# Create your views here.


@api_view(['POST'])
@authentication_classes([])
@permission_classes([])
def company_login_view(request):
    serializer = LoginSerilizer(data=request.data)
    if serializer.is_valid():
        Email = serializer.data['email']
        Password = serializer.data['password']
        try:
            user = authenticate(request, username=Email, password=Password)
            if user is not None:
                refresh = RefreshToken.for_user(user)
                return Response({'Success': 'True', 'Code': 200,
                                 'Details': {
                                     'refresh': str(refresh),
                                     'access': str(refresh.access_token),
                                 }}, status=HTTP_200_OK)
            else:
                return Response({'Success': 'False', 'Code': HTTP_400_BAD_REQUEST, 'message': 'Password and email didnt match'}, status=HTTP_400_BAD_REQUEST)

        except:       #

            return Response({'Success': 'False', 'Code': HTTP_400_BAD_REQUEST, 'message': 'Password and email didnt match'}, status=HTTP_400_BAD_REQUEST)
    return Response(data=serializer.errors, status=HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def user_auth_create(request):
    serializer = AllUsersSerilizer(data=request.data)
    if serializer.is_valid():
        email = serializer.data.get('email')
        password = serializer.data.get('password')
        phone_number = serializer.data.get('phone_number')
        first_name = serializer.data.get('first_name')
        middle_name = serializer.data.get('middle_name')
        last_name = serializer.data.get('last_name')
        status = serializer.data.get('status')

        try:
            Users.objects.get(email=email)
            return Response({'success': False, 'code': HTTP_400_BAD_REQUEST, 'message': 'email already exists'}, status=HTTP_400_BAD_REQUEST)
        except ObjectDoesNotExist:
            try:
                User.objects.create_user(
                    username=email, password=password, email=email)
            except:
                return Response({'success': False, 'code': HTTP_400_BAD_REQUEST, 'message': 'User with the email already exist'}, status=HTTP_400_BAD_REQUEST)
            my_form = Users(email=email,
                            phone_number=phone_number,
                            first_name=first_name,
                            middle_name=middle_name,
                            last_name=last_name,
                            status=status

                            )
            my_form.save()

            return Response({'success': True, 'code': HTTP_200_OK, 'message': 'Successful'}, status=HTTP_200_OK)
    return Response(data=serializer.errors, status=HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def user_auth_list(request):
    users = Users.objects.all()
    serializer = AllUsersSerilizer(users, many=True)
    return Response({'users': serializer.data},
                    status=HTTP_200_OK)


@api_view(['GET'])
def user_auth_specific(request, id):
    try:
        users = Users.objects.get(id=id)
        serializer = AllUsersSerilizer(users)
        return Response({'user': serializer.data},
                        status=HTTP_200_OK)

    except:
        return Response({'success': False, 'code': HTTP_400_BAD_REQUEST, 'message': 'Hayukooo'}, status=HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def user_auth_delete(request, id):
    try:
        users = Users.objects.get(id=id)
        users.delete()
        return Response({'success': True, 'code': HTTP_200_OK, 'message': 'Successful'}, status=HTTP_200_OK)

    except:
        return Response({'success': False, 'code': HTTP_400_BAD_REQUEST, 'message': 'Hayukooo'}, status=HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def user_auth_update(request, id):
    serializer = AllUsersSerilizer(data=request.data)
    if serializer.is_valid():
        email = serializer.data.get('email')
        password = serializer.data.get('password')
        phone_number = serializer.data.get('phone_number')
        first_name = serializer.data.get('first_name')
        middle_name = serializer.data.get('middle_name')
        last_name = serializer.data.get('last_name')
        status = serializer.data.get('status')

        try:
            user = Users.objects.get(pk=id)
            user.phone_number = phone_number
            user.first_name = first_name
            user.middle_name = middle_name
            user.last_name = last_name
            user.status = status
            user.save()

            return Response({'success': True, 'code': HTTP_200_OK, 'message': 'Successful'}, status=HTTP_200_OK)

        except ObjectDoesNotExist:
            return Response({'success': False, 'code': HTTP_400_BAD_REQUEST, 'message': 'email already exists'}, status=HTTP_400_BAD_REQUEST)

    return Response(data=serializer.errors, status=HTTP_400_BAD_REQUEST)


# Reffed By


@api_view(['POST'])
def cows_auth_create(request):
    serializer = UsersCowsSerilizer(data=request.data)
    # validating for already existing data
    if UsersCows.objects.filter(**request.data).exists():
        raise serializers.ValidationError('This data already exists')

    if serializer.is_valid():
        serializer.save()
        return Response({'Success': 'True', 'Code': 200, 'message': 'Successful'}, status=HTTP_200_OK)
    else:
        return Response(data=serializer.errors, status=HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def cows_auth_update(request, id):
    serializer = UsersCows.objects.get(pk=id)
    data = UsersCowsSerilizer(instance=serializer, data=request.data)
    if data.is_valid():
        data.save()
        return Response({'Success': 'True', 'Code': 200, 'message': 'Successful'}, status=HTTP_200_OK)
    else:
        return Response(data=data.errors, status=HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def cows_auth_list(request, id):
    roles = UsersCows.objects.filter(user_id=id)
    serializer = UsersCowsSerilizer(roles, many=True)
    return Response({'cows': serializer.data},
                    status=HTTP_200_OK)


@api_view(['GET'])
def cows_auth_specific(request, id):
    roles = UsersCows.objects.get(pk=id)
    serializer = UsersCowsSerilizer(roles)
    return Response({'cow': serializer.data},
                    status=HTTP_200_OK)


@api_view(['DELETE'])
def cows_auth_delete(request, id):
    try:
        roles = UsersCows.objects.get(pk=id)
    except UsersCows.DoesNotExist:
        return Response(status=HTTP_404_NOT_FOUND)
    if request.method == 'DELETE':
        serializer = UsersCowsSerilizer(roles,)
        role = serializer.data.get('name')

        roles.delete()

        return Response({'Success': 'True', 'Code': 200, 'message': 'Deleted Successfully'}, status=HTTP_200_OK)

    data = UsersCowsSerilizer(instance=serializer, data=request.data)
    return Response(data=data.errors, status=HTTP_400_BAD_REQUEST)



# calves
@api_view(['POST'])
def cows_calf_auth_create(request):
    serializer = UsersCowsCalvesSerilizer(data=request.data)
    # validating for already existing data
    if UsersCalves.objects.filter(**request.data).exists():
        raise serializers.ValidationError('This data already exists')

    if serializer.is_valid():
        serializer.save()
        return Response({'Success': 'True', 'Code': 200, 'message': 'Successful'}, status=HTTP_200_OK)
    else:
        return Response(data=serializer.errors, status=HTTP_400_BAD_REQUEST)


# update
@api_view(['POST'])
def cows_calf_auth_update(request, id):
    serializer = UsersCalves.objects.get(pk=id)
    data = UsersCowsCalvesSerilizer(instance=serializer, data=request.data)
    if data.is_valid():
        data.save()
        return Response({'Success': 'True', 'Code': 200, 'message': 'Successful Update'}, status=HTTP_200_OK)
    else:
        return Response(data=data.errors, status=HTTP_400_BAD_REQUEST)


# cows belonging to user
@api_view(['GET'])
def cows_calf_auth_list(request, id):
    user_calves = UsersCalves.objects.filter(calf_user_id=id)
    serializer = UsersCowsCalvesSerilizer(user_calves, many=True)
    return Response({'calves': serializer.data},
                    status=HTTP_200_OK)


@api_view(['GET'])
def cows_calf_auth_specific(request, id):
    specific_calf = UsersCalves.objects.get(pk=id)
    serializer = UsersCowsCalvesSerilizer(specific_calf)
    return Response({'calf': serializer.data},
                    status=HTTP_200_OK)


# delete calf
@api_view(['DELETE'])
def cows_calf_auth_delete(request, id):
    try:
        calf = UsersCalves.objects.get(pk=id)
    except UsersCalves.DoesNotExist:
        return Response({'Success': 'False', 'Code': HTTP_404_NOT_FOUND, 'message': 'No such calf'}, status=HTTP_200_OK)

    if request.method == 'DELETE':
        serializer = UsersCowsCalvesSerilizer(calf,)

        calf.delete()

        return Response({'Success': 'True', 'Code': 200, 'message': 'Deleted Successfully'}, status=HTTP_200_OK)

    data = UsersCowsCalvesSerilizer(instance=serializer, data=request.data)
    return Response(data=data.errors, status=HTTP_400_BAD_REQUEST)
