from django.urls import path, include
from .views import *


urlpatterns = [
    path('login', company_login_view, name='clientlogin'),

    path('create', user_auth_create, name='user_auth_create'),
    path('list', user_auth_list, name='user_auth_list'),
    path('list/<int:id>', user_auth_specific, name='user_auth_list'),
    path('delete/<int:id>', user_auth_delete, name='user_auth_list'),
    path('update/<int:id>', user_auth_update, name='user_auth_list'),


    path('cows/create', cows_auth_create, name='user_auth_create'),
    path('cows/list/<int:id>', cows_auth_list, name='user_auth_list'),
    path('cows/list/<int:id>', cows_auth_specific, name='user_auth_list'),
    path('cows/delete/<int:id>', cows_auth_delete, name='user_auth_list'),
    path('cows/update/<int:id>', cows_auth_update, name='user_auth_list'),


    path('cows-calf/create', cows_calf_auth_create, name='cows_calf_auth_create'),
    path('cows-calf/list/<int:id>', cows_calf_auth_list, name='cows_auth_list'),
    path('cows-calf/specific/<int:id>', cows_calf_auth_specific, name='cows_calf_auth_specific'),
    path('cows-calf/delete/<int:id>', cows_calf_auth_delete, name='cows_calf_auth_delete'),
    path('cows-calf/update/<int:id>', cows_calf_auth_update, name='cows_auth_update'),




]
