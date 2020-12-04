from django.urls import path
from . import views
app_name='user'
urlpatterns=[
    path('login/',views.login,name='login'),
    path('',views.index,name='index'),
    path('logout/',views.logout,name='logout'),
    path('userinfo/',views.user_info,name='userinfo'),
    path('posting/',views.posting,name='posting'),
]