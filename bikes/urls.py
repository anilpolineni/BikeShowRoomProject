from django.urls import path

from.views import (home,aboutus,dashboard,addbikes,get_bike_name,viewbike,allbikes,allcompany,updatebike,
	deletebike,myorder,customerbooking,confirmorder,orderacceptance,deleteorder,
	showdata,viewusers,deleteuser,viewcompanybikes,register,profile,updateprofile)

from django.contrib.auth import views as as_views


urlpatterns = [
	path('',home,name="home"),

	path('aboutus',aboutus,name="aboutus"),

	path('dashboard/',dashboard,name="dashboard"),

	path('addbikes/',addbikes,name="addbikes"),

	path('get_bike_name/',get_bike_name,name="get_bike_name"),

	path('updatebike/<int:id>/',updatebike,name="updatebike"),

	path('deletebike/<int:id>/',deletebike,name="deletebike"),

	path('allbikes/',allbikes,name="allbikes"),

	path('allcompany/',allcompany,name="allcompany"),

	path('showdata/',showdata,name="showdata"),

	path('viewusers/',viewusers,name="viewusers"),

	path('deleteuser/<int:id>/',deleteuser,name="deleteuser"),

	path('viewbike/<int:id>/',viewbike,name="viewbike"),

	path('viewcompanybikes/<name>',viewcompanybikes,name="viewcompanybikes"),

	path('myorder/',myorder,name="myorder"),

	path('confirmorder/<int:id>/',confirmorder,name="confirmorder"),

	path('customerbooking', customerbooking,name="customerbooking"),

	path('orderacceptance/<int:id>',orderacceptance,name="orderacceptance"),

	path('deleteorder/<int:id>/',deleteorder,name="deleteorder"),

	path('register',register,name="register"),

	path('profile',profile,name="profile"),

	path('updateprofile',updateprofile,name="updateprofile"),

	path('login',as_views.LoginView.as_view(template_name="bikes/login.html"),name="login"),

	path('logout',as_views.LogoutView.as_view(),name="logout")
	]