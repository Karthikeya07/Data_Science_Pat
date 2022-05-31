function validate(){
    var username=document.getElementById("uname").value;
    var Password=document.getElementById("pass").value;
    var pat=/^[A-z]+$/;
    if(username.trim() != "" && Password.trim() != ""){
        if(username.match(pat)){
            if(Password.length>=6){
                return true;
            }
            else{
                alert("Password lenth should be atleast 6");
                pass.focus();
                return false;
            }
        }
        else{
            alert("Username should be only in alphabets");
            username.focus();
            return false;
        }
    }
    else{
        alert("Username or Password should not be empty");
        return false;
    }      
}