from django.shortcuts import render,redirect

from django.http import HttpResponse,JsonResponse


from.forms import RegisterForm,UserUpdateForm,ProfileForm,AddBikeForm,BookingForm


from.models import UserProfile,AddBike,MyBooking

from django.contrib import messages

from django.contrib.auth.models import User

from django.contrib.auth.decorators import login_required

# Create your views here.

def home(request):
	datas=AddBike.objects.all()
	return render(request,'bikes/home.html',{'datas':datas})

def aboutus(request):
	return render(request,'bikes/aboutus.html')



def register(request):
	if request.method=="POST":
		form=RegisterForm(request.POST)
		if form.is_valid():
			form.save()
			# username=form['username'].value()
			# email=form['email'].value()
			# password=form['password1'].value()
			# sub="Account Registration"
			# body="Welcome to My Portal\n Username :-"+username+'\n Password:-'+password
			# receiver=email
			# sender=settings.EMAIL_HOST_USER
			# send_mail(sub,body,sender,[receiver])
			messages.success(request,'successfully Registred..!')
			return redirect('home')
	form=RegisterForm()
	return render(request,'bikes/register.html',{'form':form})

@login_required
def profile(request):
	user=User.objects.get(id=request.user.id)
	pro=UserProfile.objects.get(user=user)
	conext={'user':user,'pro':pro}
	return render(request,'bikes/profile.html',conext)

@login_required
def updateprofile(request):
	if request.method=="POST":
		u_form=UserUpdateForm(request.POST,instance=request.user)
		p_form=ProfileForm(request.POST,request.FILES,instance=request.user.userprofile)
		if u_form.is_valid() and p_form.is_valid():
			u_form.save()
			p_form.save()
			messages.info(request,'profile updated successfully..!')
			return redirect('profile')
	else:
		u_form=UserUpdateForm(instance=request.user)
		p_form=ProfileForm(instance=request.user.userprofile)
		conext={'u_form':u_form,'p_form':p_form}
		return render(request,'bikes/updateprofile.html',conext)
	return render(request,'bikes/updateprofile.html')

@login_required

def dashboard(request):
	customercount=User.objects.filter(is_staff=0).count()
	allbikescount=AddBike.objects.all().count()
	companynames=AddBike.objects.all().values('company')
	cnames=[]
	for i in list(companynames):
		cnames.extend(list(i.values()))
	companycount=len(set(cnames))
	bookings=MyBooking.objects.all()
	Pending=0
	Rejected=0
	Delivered=0
	for i in bookings:
		if i.tracking == "Pending":
			Pending+=1
		elif i.tracking == "Rejected":
			Rejected+=1
		elif i.tracking == "Delivered":
			Delivered+=1
	context={
	'customercount':customercount,
	'allbikescount':allbikescount,
	'companycount':companycount,
	'Pending':Pending,
	'Rejected':Rejected,
	'Delivered':Delivered}
	return render(request,'bikes/dashboard.html',context)
	



@login_required
def addbikes(request):
	if request.method=="POST":
		form=AddBikeForm(request.POST,request.FILES)
		if form.is_valid():
			bike=form.save(commit=False)
			bike.user=request.user
			bike.save()
			bikemodel=form.cleaned_data.get('bikemodel')
			messages.success(request,f"{bikemodel} is successfully Added..!")
			return redirect('allbikes')
	else:
		form=AddBikeForm()
		return render(request,'bikes/addbikes.html',{'form':form})


def get_bike_name(request):
	bike_val=list(AddBike.objects.values())
	return JsonResponse({'bike_val':bike_val})


def allbikes(request):
	data=AddBike.objects.all()
	return render(request,'bikes/allbikes.html',{'data':data})

@login_required
def allcompany(request):
	comp=AddBike.objects.all().order_by('company').values('company').distinct()
	return render(request,'bikes/allcompany.html',{'comp':comp})


@login_required
def viewcompanybikes(request,name):
	data=AddBike.objects.filter(company=name)
	return render(request,'bikes/allbikes.html',{'data':data})

@login_required
def viewbike(request,id):
	if request.method =="POST":
		bkid=request.POST.get('bikeid')
		bm=request.POST.get('bikemodel')
		bl=request.POST.get('bikelocation')
		imgs=AddBike.objects.filter(id=id).values('bikefrontimage')
		imgdict=list(imgs)[0]
		img=imgdict['bikefrontimage']
		MyBooking.objects.create(user=request.user,bikeid=bkid,bikefrontimage=img,bikemodel=bm,bikelocation=bl)
		return redirect('myorder')
	else:
		bike=AddBike.objects.get(id=id)
		return render(request,'bikes/viewbike.html',{'bike':bike})

@login_required
def showdata(request):
	data=AddBike.objects.all()
	return render(request,'bikes/showdata.html',{'data':data})

@login_required
def updatebike(request,id):
	bike=AddBike.objects.get(id=id)
	if request.method=="POST":
		form=AddBikeForm(request.POST,request.FILES,instance=bike)
		if form.is_valid():
			form.save()
			messages.warning(request,'successfully updated..!')
			return redirect('showdata')
	else:
		form=AddBikeForm(instance=bike)
		return render(request,'bikes/updatebike.html',{'bike':bike,'form':form})

@login_required
def deletebike(request,id):
	bike=AddBike.objects.get(id=id)
	if request.method=="POST":
		bike.delete()
		messages.error(request,'successfully deleted..!')
		return redirect('showdata')
	return render(request,'bikes/deletebike.html',{'bike':bike})


def myorder(request):
	order=MyBooking.objects.filter(user=request.user)
	return render(request,'bikes/myorder.html',{'orders': order})


def deleteorder(request,id):
	orders=MyBooking.objects.get(id=id)
	if request.method=="POST":
		orders.delete()
		messages.error(request,'successfully deleted..!')
		return redirect('myorder')
	return render(request,'bikes/deleteorder.html',{'orders':orders})


def confirmorder(request,id):
	orders=MyBooking.objects.get(id=id)
	if request.method=="POST":
		orders.ordername=request.POST['ordername']
		orders.document=request.FILES['document']
		orders.documenttype=request.POST['documenttype']
		orders.deliveryaddress=request.POST['address']
		orders.status="confirmed"
		orders.save()
		return redirect('myorder')
	else:
		return render(request,'bikes/orderconformation.html')


def customerbooking(request):
	cbookings=MyBooking.objects.all()
	return render(request,'bikes/customerbooking.html',{'cbookings':cbookings})

def orderacceptance(request,id):
	bookings=MyBooking.objects.get(id=id)
	bikeid_dict=list(MyBooking.objects.filter(id=id).values('bikeid'))[0]
	bikedata=AddBike.objects.get(id=bikeid_dict['bikeid'])
	if request.method=="POST":
		bookings.expecteddate=request.POST.get('expecteddate')
		bookings.tracking=request.POST.get('tracking')
		bookings.comments=request.POST.get('comments')
		bookings.save()
		return redirect('customerbooking')

	else:
		context={'bookings':bookings,'bikedata':bikedata}
		return render(request,'bikes/bookingacceptance.html',context)

@login_required
def viewusers(request):
	users = User.objects.all()
	pros=UserProfile.objects.all().values('image','gender','phno','user_id')
	pro=list(pros)
	context = {'users': users,'pro':pro}
	return render(request,'bikes/viewusers.html',context)

@login_required
def deleteuser(request,id):
	user=User.objects.get(id=id)
	if request.method=="POST":
		user.delete()
		messages.error(request,'user is successfully deleted..!')
		return redirect('viewusers')
	return render(request,'bikes/deleteuser.html',{'user':user})
