from django.contrib import admin
from .models import Zakgeld
# Rester your models here.


class ZakgeldAdmin(admin.ModelAdmin):
   list_display = ('id','person', 'task',"amount",'date_created')
   list_display_links = ('id','person', 'task',"amount",'date_created')
  



admin.site.register(Zakgeld,ZakgeldAdmin)