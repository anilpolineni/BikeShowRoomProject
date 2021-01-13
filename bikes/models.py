from django.db import models

from django.contrib.auth.models import User

from django.db.models.signals import post_save 

from django.dispatch import receiver

import os

# Create your models here.


class UserProfile(models.Model):
	gen=[('M',"Male"),('F',"Female")]

	user=models.OneToOneField(User,on_delete=models.CASCADE)
	gender=models.CharField(max_length=10,choices=gen,default="")
	image=models.ImageField(default="default.png",upload_to="pics/")
	age=models.IntegerField(default=18)
	phno=models.CharField(max_length=10)


@receiver(post_save,sender=User)
def createprofile(sender,instance,created,**kwargs):
	if created:
		UserProfile.objects.create(user=instance)



class AddBike(models.Model):

	comp=[('Bajaj','Bajaj'),('Hero','Hero'),('Honda','Honda'),('RoyalEnField','RoyalEnField')]
	
	mod=[('Pulsar 220 F','Pulsar 220 F'),('Platina 100','Platina 100'),('Bajaj CT 100','Bajaj CT 100'),
		('Glamour BS6','Glamour BS6'),('Xtreme 200S','Xtreme 200S'),('Destini 125 BS6','Destini 125 BS6'),
		('HondaShine','HondaShine'),('Honda Dio','Honda Dio'),('Honda Active','Honda Active'),
		('Bullet350','Bullet350'),('Enfield Classic 350','Enfield Classic 350'),('Enfield Meteor 350','Enfield Meteor 350')]
	fuel=[('Petrol','Petrol'),('Electric','Electric')]
	gears=[('0','0'),('4','4'),('5','5')]

	user=models.ForeignKey(User,on_delete=models.CASCADE)
	bikemodel=models.CharField(max_length=40,choices=mod)
	cost=models.FloatField(null=True)
	company=models.CharField(max_length=30,choices=comp)
	companybrand=models.ImageField(upload_to='company/')
	bikefrontimage=models.ImageField(upload_to='modelbikes/')
	bikebackimage=models.ImageField(upload_to='modelbikes/')
	bikerightimage=models.ImageField(upload_to='modelbikes/')
	bikeleftimage=models.ImageField(upload_to='modelbikes/')
	bikelocation=models.CharField(max_length=100)
	fueltype=models.CharField(max_length=20,choices=fuel)
	noofgears=models.CharField(max_length=5,choices=gears)


def content_file_name(instance, filename):
    ext = filename.split('.')[-1]
    filename = "%s_%s_%s.%s" % (instance.user.username, instance.documenttype, instance.id, ext)
    return os.path.join('documents', filename)

class MyBooking(models.Model):

	mod=[('Pulsar 220 F','Pulsar 220 F'),('Platina 100','Platina 100'),('Bajaj CT 100','Bajaj CT 100'),
		('Glamour BS6','Glamour BS6'),('Xtreme 200S','Xtreme 200S'),('Destini 125 BS6','Destini 125 BS6'),
		('HondaShine','HondaShine'),('Honda Dio','Honda Dio'),('Honda Active','Honda Active'),
		('Bullet350','Bullet350'),('Enfield Classic 350','Enfield Classic 350'),('Enfield Meteor 350','Enfield Meteor 350')]
	track=[('Delivered','Delivered'),('Pending','Pending'),('Rejected','Rejected')]

	user=models.ForeignKey(User,on_delete=models.CASCADE)
	bikeid=models.CharField(max_length=10)
	status=models.CharField(max_length=50,default='Pending')
	bikemodel=models.CharField(max_length=40,choices=mod)
	bikefrontimage=models.ImageField(upload_to='modelbikes/')
	bikelocation=models.CharField(max_length=100)
	ordername=models.CharField(max_length=30)
	expecteddate=models.DateField(null=True)
	tracking=models.CharField(max_length=50,default='awiting',choices=track)
	deliveryaddress=models.CharField(max_length=200)
	documenttype=models.CharField(max_length=30)
	document=models.FileField(upload_to=content_file_name)
	comments=models.CharField(null=True,max_length=500)




