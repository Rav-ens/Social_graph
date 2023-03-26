from django.db import models

class inputData(models.Model):
    nickname = models.CharField("Ник", max_length=100)
    hometown = models.CharField("Город", max_length=100)
    country = models.CharField("Страна", max_length=100)
    age_from = models.IntegerField("Возрас от", max_length=100)
    age_to = models.IntegerField("возраст до", max_length=100)

    def __str__(self):
        return self.nickname

