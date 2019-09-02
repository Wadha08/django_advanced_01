from django.db import models
from stores.models import Store



class Inventory(models.Model):
	name = models.CharField(max_length=150)
	store = models.ForeignKey(Store , on_delete=models.CASCADE)
	is_empty = models.BooleanField()
	last_update = models.DateTimeField(auto_now = True)


