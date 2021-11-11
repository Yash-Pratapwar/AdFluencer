// After form loads focus will go to comp_name field.
function firstfocus() {
    var comp_namef = document.registration.comp_name.focus();
    return true;
}
function validate(){
    var letters = /^\w+( \w+)*$/;
    var letterc = /^[a-zA-Z\s]*$/;
    var res = /(http(s)?:\/\/.)?(www\.)?[-a-zA-Z0-9@:%._\+~#=]{2,256}\.[a-z]{2,6}\b([-a-zA-Z0-9@:%_\+.~#?&//=]*)/g;
    var phoneno = /^\d{10}$/;
    var mail = /^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$/;
    var psw =  /^(?=.*\d)(?=.*[a-z])(?=.*[A-Z]).{6,20}$/;
    var comp_name = document.registration.comp_name.value;
    var comp_namef = document.registration.comp_name;
    var acc_handler_name = document.registration.acc_handler_name.value;
    var acc_handler_namef = document.registration.acc_handler_name;
    var acc_handler_desig = document.registration.acc_handler_desig.value;
    var acc_handler_desigf = document.registration.acc_handler_desig;
    var comp_website = document.registration.comp_website.value;
    var comp_websitef = document.registration.comp_website;
    var ph_no = document.registration.ph_no.value;
    var ph_nof = document.registration.ph_no;
    var comp_email = document.registration.comp_email.value;
    var comp_emailf = document.registration.comp_email;
    var ah_email = document.registration.ah_email.value;
    var ah_emailf = document.registration.ah_email;
    var pswd1 = document.registration.pswd1.value;
    var pswd1f = document.registration.pswd1;
    var pswd2 = document.registration.pswd2.value;
    var pswd2f = document.registration.pswd2;
    var getSelectedValue = document.querySelector('input[name="gender"]:checked');



    if (comp_name == "" || comp_name == null) {
        alert("Company name should not be empty");
        comp_namef.focus();
        return false;
    }
    else if (!comp_name.match(letterc)) {
        alert("Company name should contain only letters");
        comp_namef.focus();
        return false;
    }
    
    else if (acc_handler_name == "" || acc_handler_name == null) {
        alert("Account handler's name should not be empty");
        acc_handler_namef.focus();
        return false;
    }
    
    else if (!acc_handler_name.match(letterc)) {
        alert("Account handler's name should contain only letters");
        acc_handler_namef.focus();
        return false;
    }
    
    else if (acc_handler_desig == "" || acc_handler_desig == null) {
        alert("Account handler's designation should not be empty");
        acc_handler_desigf.focus();
        return false;
    }
    
    else if (!acc_handler_desig.match(letterc)) {
        alert("Account handler's designation should contain only letters");
        acc_handler_desigf.focus();
        return false;
    }
    
    else if (comp_website == "" || comp_website == null) {
        alert("Please enter your comp's website URL, If your company doesn't have a website just type https://sample.com");
        comp_websitef.focus();
        return false;
    }
    
    else if (!comp_website.match(res)) {
        alert("Please enter a valid URL, URL format: https://sample.com");
        comp_websitef.focus();
        return false;
    }
    
    else if (ph_no == "" || ph_no == null) {
        alert("Please enter your comp's phone number");
        ph_nof.focus();
        return false;
    }
    
    else if (!ph_no.match(phoneno)) {
        alert("Please enter a valid 10 digit phone number, format: 87XXXXXXXX");
        ph_nof.focus();
        return false;
    }
    
    else if (comp_email == "" || comp_email == null) {
        alert("Please enter your comp's E-mail ID");
        comp_emailf.focus();
        return false;
    }
    
    else if (!comp_email.match(mail)) {
        alert("Please enter a valid E-mail ID, format: xyz@gmail.com");
        comp_emailf.focus();
        return false;
    }
    
    else if (ah_email == "" || ah_email == null) {
        alert("Please enter account handler's E-mail ID");
        ah_emailf.focus();
        return false;
    }
    
    else if (!ah_email.match(mail)) {
        alert("Please enter a valid E-mail ID, format: xyz@gmail.com");
        ah_emailf.focus();
        return false;
    }
    
    else if (pswd1 == "" || pswd1 == null) {
        alert("Please enter password");
        pswd1f.focus();
        return false;
    }
    
    else if (!pswd1.match(psw)) {
        alert("Password length between 6 to 20 characters and should contain at least one numeric digit, one uppercase and one lowercase letter");
        pswd1f.focus();
        return false;
    }
    
    else if (pswd2 == "" || pswd2 == null) {
        alert("Please enter your password again");
        pswd2f.focus();
        return false;
    }
    
    else if (!pswd2.match(pswd1)) {
        alert("Password do not match");
        pswd2f.focus();
        return false;
    }
    
    else if (getSelectedValue == null) {
        alert("Please choose your gender.");
        return false;
    }
}

