from django.contrib import admin
from .models import HomePage, AboutPageInfo, AboutChef, MenuCategory, Menu, Book
# Register your models here.

admin.site.register(HomePage)
admin.site.register(AboutPageInfo)
admin.site.register(AboutChef)
admin.site.register(MenuCategory)
admin.site.register(Menu)
admin.site.register(Book)
