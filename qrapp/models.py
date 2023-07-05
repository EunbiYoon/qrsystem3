from django.db import models

# Create your models here.
class QRCodeData(models.Model):
    code_data=models.CharField(max_length=255)
    arriving_at=models.DateTimeField(auto_now_add=True)
    receiver=models.CharField(max_length=255)
    receiver_check=models.BooleanField(default=False)
    admin_check=models.BooleanField(default=False)
    receiver_at=models.DateTimeField(blank=True, null=True)
    admin_at=models.DateTimeField(blank=True,null=True)

    def __str__(self):
        return str(self.code_data)+ ' | Arrived at ' + str(self.arriving_at.strftime("%m/%d %H:%M"))
    class Meta:
        verbose_name_plural='QR Scanning Data'

