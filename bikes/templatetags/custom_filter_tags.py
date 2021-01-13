from django import template

register = template.Library() 

from bikes.models import AddBike

@register.filter(name="companyimage")
def companyimage(name):
	img=AddBike.objects.filter(company=name).values('companybrand')
	imgdict=img[0]
	return '/images/'+imgdict['companybrand']



@register.filter(name="mobileno")
def mobileno(userlist,id):
	for mb in userlist:
		if mb['user_id'] == id:
			return mb['phno']


@register.filter(name="gen")
def gen(userlist,id):
	for mb in userlist:
		if mb['user_id'] == id:
			return mb['gender']

@register.filter(name="userimage")
def userimage(userlist,id):
	for mb in userlist:
		if mb['user_id'] == id:
			return '/images/'+mb['image']