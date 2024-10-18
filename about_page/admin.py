from django.contrib import admin
from solo.admin import SingletonModelAdmin
from .models import AboutPage

@admin.register(AboutPage)
class AboutPageAdmin(SingletonModelAdmin):
    pass