const aname = document.querySelector('.account-name');
const name_check = aname.textContent;
if (name_check.indexOf(' ') >= 0) {
    const accountdiv = document.querySelector('.account-info');
    const login_button = document.querySelector('.login-button');
    accountdiv.classList.add('active-account');
    login_button.classList.add('active-button');
}

let reservationcheck;
let cancellationdatecheck;
let changedetailsdatecheck;
let updatestatus;

reservationcheck = document.querySelector('.reservationidcheck');
cancellationdatecheck = document.querySelector('.cancellationdatecheck');
changedetailsdatecheck = document.querySelector('.changedetailsdatecheck');
updatestatus = document.querySelector('.updatestatus');

if (reservationcheck.textContent == "incorrect") {
    alert("Invalid reservation ID !");
}


if (cancellationdatecheck.textContent == "incoorectdate") {
    alert("Cannot cancel past or ongoing travel.");
}



if (changedetailsdatecheck.textContent == "incoorectdate") {
    console.log(changedetailsdatecheck.textContent);
    alert("Cannot change details of past or ongoing travel.");
}


if (updatestatus.textContent == "successful") {
    alert("The passenger details have been successfully updated.");
}

