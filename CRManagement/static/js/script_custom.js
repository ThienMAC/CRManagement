function confirmPassword() {
    if(document.getElementById("password").value==
    document.getElementById("re_password").value){
        document.getElementById("Message").style.color = "Green";
        document.getElementById("Message").innerHTML = "Passwords match!"
    }
    else {
        document.getElementById("Message").style.color = "Red";
        document.getElementById("Message").innerHTML = "Passwords do NOT match!"
    }
}