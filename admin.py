"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

from django.contrib import admin
from tf.models import User,Equipment,LendEquipment,LendingEquipment,GiveEquipment,DeleteEquipment
class EquipmentAdmin(admin.ModelAdmin):
    list_display = ('Name', 'Number', 'Model','Price','Prodate','Buydate')
   
 
admin.site.register(User)
admin.site.register(Equipment,EquipmentAdmin)
admin.site.register(LendEquipment)
admin.site.register(LendingEquipment)
admin.site.register(GiveEquipment)
admin.site.register(DeleteEquipment)
