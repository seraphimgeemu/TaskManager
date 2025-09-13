from django.contrib import admin
from .models import Tarea
# Register your models here.

class TareaAdmin(admin.ModelAdmin):
    readonly_fields = ('created_at',)

admin.site.register(Tarea, TareaAdmin)
