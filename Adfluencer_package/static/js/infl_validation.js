// console.log("this form validation")
// alert("validation.js loaded successfully!")
function validate(){
    var letters = /^[a-zA-Z]+$/;
    var lettersf =  /^(([a-zA-Z]*, )|([a-zA-Z]*))*$/;
    // var lettersf = /^([a-zA-Z]+)(,([a-zA-Z]+))+$/;
    var res = /(http(s)?:\/\/.)?(www\.)?[-a-zA-Z0-9@:%._\+~#=]{2,256}\.[a-z]{2,6}\b([-a-zA-Z0-9@:%_\+.~#?&//=]*)/g;
    var phoneno = /^\d{10}$/;
    var mail = /^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$/;
    var psw =  /^(?=.*\d)(?=.*[a-z])(?=.*[A-Z]).{6,20}$/;
    var fname = document.registration.fname.value;
    var fnam = document.registration.fname;
    var lname = document.registration.lname.value;
    var lnam = document.registration.lname;
    var smh = document.registration.smh.value;
    var smhf = document.registration.smh;
    var ph_no = document.registration.ph_no.value;
    var ph_nof = document.registration.ph_no;
    var inf_email = document.registration.inf_email.value;
    var inf_emailf = document.registration.inf_email;
    var pswd1 = document.registration.pswd1.value;
    var pswd1f = document.registration.pswd1;
    var pswd2 = document.registration.pswd2.value;
    var pswd2f = document.registration.pswd2;
    var age = document.registration.age.value;
    var agef = document.registration.age;
    var getSelectedValue = document.querySelector('input[name="gender"]:checked');
    var inf_categories = document.registration.inf_categories.value;
    var inf_categoriesf = document.registration.inf_categories;



    if (fname == "" || fname == null) {
        alert("First name should not be empty");
        fnam.focus();
        return false;
    }
    else if (!fname.match(letters)) {
        alert("First name should contain only letters");
        fnam.focus();
        return false;
    }
    
    else if (lname == "" || lname == null) {
        alert("Last name should not be empty");
        lnam.focus();
        return false;
    }
    
    else if (!lname.match(letters)) {
        alert("Last name should contain only letters");
        lnam.focus();
        return false;
    }
    
    else if (smh == "" || smh == null) {
        alert("Please enter your social media handle");
        smhf.focus();
        return false;
    }
    
    else if (!smh.match(res)) {
        alert("Please enter a valid URL, URL format: https://sample.com");
        smhf.focus();
        return false;
    }
    
    else if (ph_no == "" || ph_no == null) {
        alert("Please enter your phone number");
        ph_nof.focus();
        return false;
    }
    
    else if (!ph_no.match(phoneno)) {
        alert("Please enter a valid 10 digit phone number, format: 87XXXXXXXX");
        ph_nof.focus();
        return false;
    }
    
    else if (inf_email == "" || inf_email == null) {
        alert("Please enter your E-mail ID");
        inf_emailf.focus();
        return false;
    }
    
    else if (!inf_email.match(mail)) {
        alert("Please enter a valid E-mail ID, format: xyz@gmail.com");
        inf_emailf.focus();
        return false;
    }

    else if (inf_categories == "" || inf_categories == null) {
        alert("Categories should not be empty");
        inf_categoriesf.focus();
        return false;
    }
    
    else if (!inf_categories.match(lettersf)) {
        alert("Categories should contain only letters");
        inf_categoriesf.focus();
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
    
    else if (age == "" || age == null) {
        alert("Please enter your age");
        agef.focus();
        return false;
    }
    
    else if (!(age > 13 && age < 100)) {
        alert("The age must be a number between 13 and 100");
        agef.focus();
        return false;
    }

    else if (getSelectedValue == null) {
        alert("Please choose your gender.");
        return false;
    }
}

// After form loads focus will go to First name field.
function firstfocus() {
    var fnam = document.registration.fname.focus();
    return true;
}
// // This function will validate First name.
// function fnam_validation(fn) {
//     var letters = /^[a-zA-Z]+$/;
//     var fname = document.registration.fname.value;
//     var fnam = document.registration.fname;

//     if (fname == "" || fname == null) {
//         alert("First name should not be empty");
//         if (fn.value.match(letters)) {
//             return true;
//         }
//         else {
//             alert("First name should contain only letters");
            
//             return false;
//         }
//     }
//     // Focus goes to next field i.e. lname.
//     document.registration.lname.focus();
//     return true;
// }
// function lnam_validation(ln) {
//     var letters = /^[a-zA-Z]+$/;
//     var lname = document.registration.lname.value;
//     var lnam = document.registration.lname;

//     if (lname == "" || lname == null) {
//         alert("Last name should not be empty");
//         if (ln.value.match(letters)) {
//             return true;
//         }
//         else {
//             alert("Last name should contain only letters");
            
//             return false;
//         }
//     }
    

//     // Focus goes to next field i.e. lname.
//     // document.registration.lname.focus();
//     // return true;
// }
// // This function will validate Password.
// function passid_validation(mx, my) {
//     var passid = document.registration.passid;
//     var passid_len = passid.value.length;
//     if (passid_len == 0 || passid_len >= my || passid_len < mx) {
//         alert("Password should not be empty / length be between " + mx + " to " + my);
//         passid.focus();
//         return false;
//     }
//     // Focus goes to next field i.e. Name.
//     document.registration.username.focus();
//     return true;
// }
// // This function will validate Name.
// function allLetter() {
//     var uname = document.registration.username;
//     var letters = /^[A-Za-z]+$/;
//     if (uname.value.match(letters)) {
//         // Focus goes to next field i.e. Address.
//         document.registration.address.focus();
//         return true;
//     }
//     else {
//         alert('Username must have alphabet characters only');
//         uname.focus();

//         return false;
//     }
// }
// // This function will validate Address.
// function alphanumeric() {
//     var uadd = document.registration.address;
//     var letters = /^[0-9a-zA-Z]+$/;
//     if (uadd.value.match(letters)) {
//         // Focus goes to next field i.e. Country.
//         document.registration.country.focus();
//         return true;
//     }
//     else {
//         alert('User address must have alphanumeric characters only');
//         uadd.focus();
//         return false;
//     }
// }
// // This function will select country name.
// function countryselect() {
//     var ucountry = document.registration.country;
//     if (ucountry.value == "Default") {
//         alert('Select your country from the list');
//         ucountry.focus();
//         return false;
//     }
//     else {
//         // Focus goes to next field i.e. ZIP Code.
//         document.registration.zip.focus();
//         return true;
//     }
// }
// // This function will validate ZIP Code.
// function allnumeric() {
//     var uzip = document.registration.zip;
//     var numbers = /^[0-9]+$/;
//     if (uzip.value.match(numbers)) {
//         // Focus goes to next field i.e. email.
//         document.registration.email.focus();
//         return true;
//     }
//     else {
//         alert('ZIP code must have numeric characters only');
//         uzip.focus();
//         return false;
//     }
// }
// // This function will validate Email.
// function ValidateEmail() {
//     var uemail = document.registration.email;
//     var mailformat = /^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$/;
//     if (uemail.value.match(mailformat)) {
//         document.registration.desc.focus();
//         return true;
//     }
//     else {
//         alert("You have entered an invalid email address!");
//         uemail.focus();
//         return false;
//     }
// }
