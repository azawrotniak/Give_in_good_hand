from django.contrib import admin

# Register your models here.
from .models import Category, Donation, Institution

admin.site.register(Category)
admin.site.register(Donation)
admin.site.register(Institution)


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)


class DonationAdmin(admin.ModelAdmin): # https://docs.djangoproject.com/pl/3.2/intro/tutorial07/
    list_display = ('user', 'institution', 'pick_up_date')