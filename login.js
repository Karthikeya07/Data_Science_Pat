function login(){
	var userName=document.getElementById("un").value;
	var Password=document.getElementById("pass").value;
	if(userName=="" || Password=="")
		alert("Empty values are not allowed");
	else if(userName=="Karthikeya" && Password=="19881A0597")
		window.location.href="home.html";
	else
		window.location.href="error.html";
} 