from django.urls import path

from .import views


app_name = 'bankapp'
urlpatterns = [
    path('',views.home,name='home'),
    path('login', views.login, name='login'),
    path('register',views.register,name='register'),
    path('kottayam', views.kottayam, name='kottayam'),
    path('alappuzha', views.alappuzha, name='alappuzha'),
    path('ernakulam', views.ernakulam, name='ernakulam'),
    path('idukki', views.idukki, name='idukki'),
    path('kannur', views.kannur, name='kannur'),
    path('newform',views.newform,name='newform'),
    path('form',views.form,name='form'),
    path('ok',views.ok,name='ok'),

]
