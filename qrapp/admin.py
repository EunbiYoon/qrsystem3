from django.contrib import admin
from .models import QRCodeData

class QRCodeDataAdmin(admin.ModelAdmin):
    list_display=['code_data','arriving_at','receiver','receiver_check','admin_check','receiver_at','admin_at']

# Register your models here.
admin.site.register(QRCodeData, QRCodeDataAdmin)
