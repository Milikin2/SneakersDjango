from django.contrib import admin
from django.urls import path, include
from Sneakers import views

urlpatterns = [
    path('Admin', admin.site.urls),
    path('admin/', views.admin, name='admin'),
    path('', views.index, name='index'),
    path('home.html/', views.home, name='home'),
    path('cabinet.html/', views.cabinet, name='cabinet'),
    path('favs.html/', views.favs, name='favs'),
    path('cabinetData.html/', views.cabinetData, name='cabinetData'),
    path('addProduct.html/', views.addProduct, name='addProduct'),
    path('json/', views.json, name='json'),
    path('workers/', views.workers, name='workers'),
    path('users/', views.users, name='users'),
    path('createUser', views.createUser),
]
