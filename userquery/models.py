from django.db import models


class SumoLogic(models.Model):
    Query = models.CharField(max_length=200)
    From_Date_Time = models.TextField()
    To_Date_Time = models.TextField()

    def __str__(self):
        return self.Query