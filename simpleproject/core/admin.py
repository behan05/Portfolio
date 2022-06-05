
from django.contrib import admin
from core.models import SignupTB

# Register your models here.

@admin.register(SignupTB)
class SignupTBAdmin(admin.ModelAdmin):
    list_display = ('id','Username','Email','Password','CnfPassword')