from django.contrib import admin
from solo.admin import SingletonModelAdmin
from .models import WorksPage, Work


@admin.register(WorksPage)
class WorksPageAdmin(SingletonModelAdmin):
    pass

@admin.register(Work)
class WorkAdmin(admin.ModelAdmin):
    pass