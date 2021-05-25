from django.contrib import admin
from .models import ValuesStored
# Register your models here.
@admin.register(ValuesStored)
class InputValues(admin.ModelAdmin):
    list_display = ('id', 'user','timeStamp', 'inputValues')