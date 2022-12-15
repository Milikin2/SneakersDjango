from django.shortcuts import render
from .models import Product
from .models import User
from django.http import JsonResponse


# Create your views here.
def home(request):
    return render(request, 'home.html')


def cabinet(request):
    return render(request, 'cabinet.html')


def favs(request):
    return render(request, 'favs.html')


def cabinetData(request):
    return render(request, 'cabinetData.html')


def json(request):
    data = list(Product.objects.values())
    return JsonResponse(data, safe=False)


def users(request):
    user = list(User.objects.values())
    return JsonResponse(user, safe=False)


def createUser(request):
    model = User()
    model.userName = request.POST['userName']
    model.userLastname = request.POST['userLastName']
    model.userLogin = request.POST['userLogin']
    model.userPassword = request.POST['userPassword']
    model.userEmail = request.POST['userEmail']
    model.userPhone = request.POST['userPhone']
    model.save()
    return render(request, 'cabinet.html')
