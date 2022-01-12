from django.db import models


class LongitudeLatitude(models.Model):
   longitude = models.CharField(max_length = 50)
   latitude = models.CharField(max_length = 50)
   name = models.CharField(max_length = 100)

   class Meta:
      app_label = 'LongitudeLatitude'
      db_table = 'LongitudeLatitude'
