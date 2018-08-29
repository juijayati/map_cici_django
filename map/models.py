from django.db import models
from datetime import datetime, timedelta
from django.utils.timesince import timesince
# Create your models here.



class dummy_table(models.Model):
    dtordinal = models.DecimalField(max_digits=25, decimal_places=15)
    #start = models.TimeField(auto_now_add=True)
    name = models.CharField(max_length=125)
    lat = models.DecimalField(max_digits=20, decimal_places=17)
    lng = models.DecimalField(max_digits=20, decimal_places=17)
    mlabel = models.CharField(max_length=100)

    def date(self):
        days = self.dtordinal % 1
        hours = days % 1 * 24
        minutes = hours % 1 * 60
        seconds = minutes % 1 * 60
        py_datetime= datetime.fromordinal(int(self.dtordinal)) \
               + timedelta(days=int(days)) \
               + timedelta(hours=int(hours)) \
               + timedelta(minutes=int(minutes)) \
               + timedelta(seconds=round(seconds)) \
               - timedelta(days=366)
        return py_datetime.date()

    def time(self):
        days = self.dtordinal % 1
        hours = days % 1 * 24
        minutes = hours % 1 * 60
        seconds = minutes % 1 * 60
        py_datetime = datetime.fromordinal(int(self.dtordinal)) \
                      + timedelta(days=int(days)) \
                      + timedelta(hours=int(hours)) \
                      + timedelta(minutes=int(minutes)) \
                      + timedelta(seconds=round(seconds)) \
                      - timedelta(days=366)
        return py_datetime.time()


