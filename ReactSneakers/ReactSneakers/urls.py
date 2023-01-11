from django.contrib import admin
from django.urls import path, include
from Sneakers import views

urlpatterns = [
    path('admin', admin.site.urls),
    path('', views.home, name='home'),
    path('cabinet.html/', views.cabinet, name='cabinet'),
    path('favs.html/', views.favs, name='favs'),
    path('cabinetData.html/', views.cabinetData, name='cabinetData'),
    path('json/', views.json, name='json'),
    path('users/', views.users, name='users'),
    path('createUser/', views.createUser, name='createUser'),
    path('cartOrder', views.cartOrder, name='cartOrder'),
]
