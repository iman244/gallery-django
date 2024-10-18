from django.contrib import admin
from solo.admin import SingletonModelAdmin
from .models import HomePage, SocialMedia

class SocialMediaInline(admin.TabularInline):
    model = SocialMedia
    extra = 1

@admin.register(HomePage)
class HomePageAdmin(SingletonModelAdmin):
    inlines = [SocialMediaInline]