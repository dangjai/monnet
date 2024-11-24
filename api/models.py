from django.db import models

class MNStatus(models.Model):
    Temp = models.FloatField()
    Humi = models.FloatField()
    Volt = models.FloatField()
    date_updated = models.DateTimeField(auto_now=True)

    # def __str__(self):
    #     return self.date_updated
    
class MNSetup(models.Model):
    TelegramToken = models.CharField(max_length=46)
    TelegramChatId = models.CharField(max_length=11)
    TempAlert = models.IntegerField()
    TempStatus = models.IntegerField()
    HumiAlert = models.IntegerField()
    HumiStatus = models.IntegerField()
    VoltAlert = models.IntegerField()
    VoltStatus = models.IntegerField()


# Create your models here.