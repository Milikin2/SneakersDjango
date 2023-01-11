from django.contrib import admin
from .models import Product
from .models import User
from .models import Bought

# Register your models here.

admin.site.register(Product)
admin.site.register(User)
admin.site.register(Bought)
