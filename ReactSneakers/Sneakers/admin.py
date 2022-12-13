from django.contrib import admin
from .models import Product
from .models import Worker
from .models import User
from .models import Fav
from .models import Bought

# Register your models here.

admin.site.register(Product)
admin.site.register(Worker)
admin.site.register(User)
admin.site.register(Fav)
admin.site.register(Bought)
