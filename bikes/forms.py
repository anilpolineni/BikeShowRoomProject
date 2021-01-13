from django import forms

from.models import UserProfile,AddBike,MyBooking

from django.contrib.auth.models import User

from django.contrib.auth.forms import UserCreationForm



class RegisterForm(UserCreationForm):
	password1 = forms.CharField(widget=forms.PasswordInput(attrs={
		'class':'form-control',
		'placeholder':'Enter Password'
		}))
	password2 = forms.CharField(widget=forms.PasswordInput(attrs={
		'class':'form-control',
		'placeholder':'Enter Confrim Password'
		}))
	class Meta:
		model=User

		fields=['first_name','last_name','username','email']

		widgets={
			"first_name":forms.TextInput(attrs={'class':'form-control first_name','placeholder':"Enter Your FName","required":True}),
			"last_name":forms.TextInput(attrs={'class':"form-control last_name",'placeholder':"Enter Your LName","required":True}),
			"username":forms.TextInput(attrs={'class':"form-control username ",'placeholder':"Enter Your username"}),
			"email":forms.EmailInput(attrs={'class':"form-control email","placeholder":"Enter Your Email"}),
		}

class UserUpdateForm(forms.ModelForm):
	class Meta:
		model=User

		fields=['first_name','last_name','username','email']

		widgets={
			"first_name":forms.TextInput(attrs={'class':'form-control col-md-4','placeholder':"Enter Your FName","required":True}),
			"last_name":forms.TextInput(attrs={'class':"form-control last_name col-md-4",'placeholder':"Enter Your LName","required":True}),
			"username":forms.TextInput(attrs={'class':"form-control username col-md-4 ",'placeholder':"Enter Your username"}),
			"email":forms.EmailInput(attrs={'class':"form-control email col-md-4","placeholder":"Enter Your Email"}),
		}


class ProfileForm(forms.ModelForm):
	class Meta:
		model = UserProfile

		fields=['gender','image','age','phno']


		widgets={

		#"gender":forms.RadioSelect(attrs={'class':'custom-control-inline custom-radio radio-inline gender','type':"radio"}),
		"age":forms.NumberInput(attrs={'placeholder':"Enter Your Age",'class':"form-control"}),
		"phno":forms.TextInput(attrs={'placeholder':"Enter Your Phno",'class':"form-control"}),
		
		}

   
class AddBikeForm(forms.ModelForm):
	class Meta:

		model=AddBike

		fields=['company','bikemodel','fueltype','companybrand','bikefrontimage','bikebackimage',
		'bikerightimage','bikeleftimage','cost','bikelocation','noofgears']



class BookingForm(forms.ModelForm):
	class Meta:

		model=MyBooking

		fields=['bikemodel','bikelocation']

