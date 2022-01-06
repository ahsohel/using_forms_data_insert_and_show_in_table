from django.contrib import admin
from . models import form_models

# Register your models here\.



class dis_form_models(admin.ModelAdmin):
    list_display = ['name', 'phone']

admin.site.register(form_models, dis_form_models)