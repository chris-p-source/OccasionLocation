from django.db import models
from accounts.models import User 
#from users.models import CustomUser 

# Create your models here.


class Event(models.Model):

	title = models.CharField(max_length=50)
	date = models.DateField()
	address = models.CharField(max_length=50)
	town = models.CharField(max_length=30)
	county = models.CharField(max_length=20)
	postcode = models.CharField(max_length=6)
	starttime = models.TimeField()
	genre = models.CharField(max_length=10)
	description = models.CharField(max_length=1024)
	price = models.DecimalField(decimal_places=2, max_digits=1000)
	duration = models.DecimalField(decimal_places=0, max_digits=1000)
	host = models.ForeignKey(User, on_delete=models.CASCADE)
	
	def __str__(self):
		return self.title



class EventAttendance(models.Model):
    person_key = models.ForeignKey(User, on_delete=models.CASCADE)
    event_key = models.ForeignKey(Event, on_delete=models.CASCADE)
    

    def __str__(self):
        return "%s - %s" % (self.event_key, self.person_key)