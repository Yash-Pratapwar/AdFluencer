console.log('test')
function validateform() {
    var company_name = document.forms["registration"]["company_name"];
    let ah_name = document.registration.acc_handler_name;
    let ah_desig = document.registration.acc_handler_desig.value;
    let num = document.registration.rollno.value;
    let pw1 = document.registration.pswd1.value;
    let pw2 = document.registration.pswd2.value;
    let dept = document.registration.r_dept.value;
    let age = document.registration.age.value;
    let email = document.registration.email.value;
    let getSelectedValue = document.querySelector('input[name="gender"]:checked');
    

    if (company_name.value == null || company_name.value == "") {
        alert("Company name can't be blank");
        // ufname.focus();
        return false;
    } else if (ah_name == null || ah_name == "") {
        alert("Account handler's name can't be blank");
        // ah_name.focus();
        return false;
    } else if (ah_desig == null || acc_handler_desig == "") {
        alert("Account handler's name can't be blank");
        // ah_name.focus();
        return false;
    } else if (dept == null || dept == "") {
        alert("Please select your Department");
        // ah_name.focus();
        return false;
    } else if (num == null || num == "") {
        alert("Roll no. can't be left blank");
        // num.focus();
        return false;
    } else if (num.length < 7) {
        alert("Roll no. can't be less than 7 digits.");
        // num.focus();
        return false;
    } else if (isNaN(num)) {
        document.getElementsByName("rollno").innerHTML = "Enter numeric value only.";
        // num.focus();
        return false;
    } else if (email == "") {
        alert("Please enter a valid e-mail address.");
        // email.focus();
        return false;
    } else if (pw1 == null || pw1 == "") {
        alert("Password can't be left blank.");
        // password.focus();
        return false;
    } else if (pw1.length < 6) {
        alert("Password must be at least 6 characters long.");
        // password.focus();
        return false;
    } else if (pw2 == null || pw2 == "") {
        alert("Please enter your password again.");
        // password.focus();
        return false;
    } else if (pw2.length < 6) {
        alert("Password must be at least 6 characters long.");
        // password.focus();
        return false;
    } else if (pw1 != pw2) {
        alert("Password must be same!");
        // pw1.focus();
        return false;
    } else if (age == null || age == "") {
        alert("Age can't be left blank.");
        // age.focus();
        return false;
    } else if (age < 18 || age > 100) {
        alert("Age can't be less than 18 or more than 100.");
        // age.focus();
        return false;
    } else if (getSelectedValue == null) {
        alert("Please choose your gender.");
        return false;
    } else {
        alert('Form Succesfully Submitted');
        window.location.reload()
        return true;
    }
}
