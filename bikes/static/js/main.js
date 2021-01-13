$.ajax({
	type:"GET",
	url:'/get_bike_name/',
	success:function(response){
		console.log(response)
	},
	error:function(error){
		console.log(error)
	}

})