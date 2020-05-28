"""voidTech URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from userApp.models import User as Shopper, Wishlist
from productApp.models import Brand, OS, Processor, Memory, Graphics_card, Storage, Category, Product

class ShopperAdmin(admin.ModelAdmin):
    pass
admin.site.register(Shopper, ShopperAdmin)
class BrandAdmin(admin.ModelAdmin):
    pass
admin.site.register(Brand, BrandAdmin)
class OSAdmin(admin.ModelAdmin):
    pass
admin.site.register(OS, OSAdmin)
class ProcessorAdmin(admin.ModelAdmin):
    pass
admin.site.register(Processor, ProcessorAdmin) 
class MemoryAdmin(admin.ModelAdmin):
    pass
admin.site.register(Memory, MemoryAdmin)
class Graphics_cardAdmin(admin.ModelAdmin):
    pass
admin.site.register(Graphics_card, Graphics_cardAdmin)
class StorageAdmin(admin.ModelAdmin):
    pass
admin.site.register(Storage, StorageAdmin)
class CategoryAdmin(admin.ModelAdmin):
    pass
admin.site.register(Category, CategoryAdmin)
class ProductAdmin(admin.ModelAdmin):
    pass
admin.site.register(Product, ProductAdmin)
class WishlistAdmin(admin.ModelAdmin):
    pass
admin.site.register(Wishlist, WishlistAdmin)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('productApp.urls')),
    path('user/', include('userApp.urls'))
]
