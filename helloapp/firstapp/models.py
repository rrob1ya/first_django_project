from dataclasses import field
from unittest import result
from django.db import models

class Test(models.Model):
    field1 = models.IntegerField()
    field2 = models.IntegerField()

class SumTwoIntegers(models.Model):
    field1 = models.IntegerField()
    field2 = models.IntegerField()
    result = models.IntegerField()
    
