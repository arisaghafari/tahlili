from django.contrib import admin
from .models import Supplier, Product, Profile

# Register your models here.
admin.site.register(Supplier)
admin.site.register(Product)
admin.site.register(Profile)
