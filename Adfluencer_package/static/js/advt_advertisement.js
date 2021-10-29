// After form loads focus will go to Company name field.
function firstfocus() {
    var descf = document.advertisements.desc.focus();
    return true;
}
function validate() {
    var desc = document.advertisements.desc.value;
    var descf = document.advertisements.desc;
    var brand = document.advertisements.brand.value;
    var brandf = document.advertisements.brand;
    var deadline = document.advertisements.deadline.value;
    var deadlinef = document.advertisements.deadline;
    var prdt_sp = document.advertisements.prdt_sp.value;
    var prdt_spf = document.advertisements.prdt_sp;
    var age_grp = document.advertisements.age_grp.value;
    var age_grpf = document.advertisements.age_grp;
    var prdt_imgs = document.advertisements.prdt_imgs.value;
    var prdt_imgsf = document.advertisements.prdt_imgs;
    



    if (desc == "" || desc == null) {
        alert("Please enter product description.");
        descf.focus();
        return false;
    }

    else if (brand == "" || brand == null) {
        alert("Please enter brand name.");
        brandf.focus();
        return false;
    }

    else if (deadline == "" || deadline == null) {
        alert("Please enter deadline.");
        deadlinef.focus();
        return false;
    }

    else if (prdt_sp == "" || prdt_sp == null) {
        alert("Please enter product selling points.");
        prdt_spf.focus();
        return false;
    }
    
    else if (age_grp == "" || age_grp == null) {
        alert("Please enter age group targeted.");
        age_grpf.focus();
        return false;
    }

    else if (prdt_imgs == "" || prdt_imgs == null) {
        alert("Please upload a valid image file (JPEG/JPG/PNG/GIF).");
        prdt_imgsf.focus();
        return false;
    }    
}

