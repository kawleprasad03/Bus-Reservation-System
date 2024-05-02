const sel1 = document.getElementById("from");
const sel2 = document.getElementById("to");

sel1.addEventListener("change", function() {
  toggleOptions(this, sel2);
});

sel2.addEventListener("change", function() {
  toggleOptions(this, sel1);
});

function toggleOptions(sourceSelect, targetSelect) {
  const selectedValue = sourceSelect.value;

  // Reset all options in the target select to be visible
  for (const option of targetSelect.options) {
    option.style.display = "";
  }

  // Hide the corresponding option in the target select
  const targetOption = targetSelect.querySelector(`option[value="${selectedValue}"]`);
  if (targetOption) {
    targetOption.style.display = "none";
  }
}


// input date onfoucs event to display calender
const inputDate = document.getElementById("travel-date");

inputDate.addEventListener("focus",function () {
  if (this.getAttribute("type")==="date") {
    this.showPicker();
  }
});


// set min and max date in inputDate filed
const currentDate = new Date(); // Get the current date
currentDate.setDate(currentDate.getDate() + 1); // Set it to the next day
const nextDay = currentDate.toISOString().split('T')[0]; // Convert to YYYY-MM-DD format
inputDate.setAttribute('min', nextDay); // Set the minimum date allowed as the next day

const maxDate = new Date(currentDate.getFullYear(), currentDate.getMonth() + 2, 0); // Get the date 2 months later
const maxDateString = maxDate.toISOString().split('T')[0];
inputDate.setAttribute('max', maxDateString);


//for bacground blur and display login page
const background = document.querySelector('.background');
const login = document.querySelector('.login')
const logButton = document.querySelector('.login-button');
const close1 = document.querySelector('.close1')
logButton.addEventListener('click', () => {
    background.style.filter = 'blur(5px)';
    login.classList.add('active-login');
})

close1.addEventListener('click', () => {
    background.style.filter = 'blur(0)';
    login.classList.remove('active-login');
})

// To display sign up and close
const signup = document.querySelector('.signup');
const signup_link = document.querySelector('#sign-up');
const close2 = document.querySelector('.close2');
signup_link.addEventListener('click', () => {
  // login.classList.remove('active-login');
  signup.classList.add('active-signup');
})

close2.addEventListener('click' , (event) => {
  background.style.filter = 'blur(0)';
  signup.classList.remove('active-signup');
})


//sign up page password confirmation 
const confirmPassword = document.querySelector('#cpwd');
confirmPassword.addEventListener('keyup' , () => {
  const password = document.querySelector('#pwd').value;
  const confirmationvalue = confirmPassword.value;
  if (password != confirmationvalue) {
    confirmPassword.style.borderColor = 'red';
  }
  else {
    confirmPassword.style.borderColor = 'blue';
  }
})

const genderselect = document.querySelector('#gender');
const submit = document.querySelector('#save');
submit.addEventListener('click' , (event) => {
  const confirmPassword = document.getElementById('cpwd');
  const computedStyle = window.getComputedStyle(confirmPassword);
  const borderColor = computedStyle.getPropertyValue('border-color');

  if (borderColor === 'rgb(255, 0, 0)') { 
    event.preventDefault(); // Prevent form submission
    alert('password incorrect!');
  }

  // gender check
  const genderselectvalue = genderselect.value;
  if (genderselectvalue === "select"){
    event.preventDefault();
    alert('Please select gender!');
  }
})

// First name take only alphabetical characters
const fname = document.querySelector('#fname');
fname.addEventListener('input' , () => {
  const fnamevalue = fname.value;
  const alphvalue = fnamevalue.replace(/[^a-zA-Z]/g,'');
  fname.value = alphvalue;
})

// Last name take only alphabetical characters
const lname = document.querySelector('#lname');
lname.addEventListener('input' , () => {
  const lnamevalue = lname.value;
  const alphvalue = lnamevalue.replace(/[^a-zA-Z]/g,'');
  lname.value = alphvalue;
})

// Age not greater than 100 and only take digits
const age = document.querySelector('#age');
age.addEventListener('input', () => {
  const agevalue = age.value;
  const numericvalue = agevalue.replace(/\D/g,'');
  age.value = numericvalue;
  if (age.value > 100){
    alert('Please provide valid age!');
    age.value = '';
  }
})

// Phone Number not more than 10 digits and only take digits
const phone = document.querySelector('#phone');
phone.addEventListener('input', () => {
  const phonevalue = phone.value;
  const numericvalue = phonevalue.replace(/\D/g,'');
  phone.value = numericvalue;
  if (phone.value.length > 10){
    phone.value = phone.value.slice(0,10);
  }
})

// Email validation
const email = document.querySelector('#email');
email.addEventListener('focusout', () => {
  const emailcheck = email.value;
  const emailpattern = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
  if (!emailpattern.test(emailcheck)){
    alert('Please enter a valid email address!');
  }
}) 

//show password 
const logpassword = document.querySelector('#lpassword');
const signpassword = document.querySelector('#pwd');
const signconfpassword = document.querySelector('#cpwd'); 
const eyeicon1 = document.querySelector('#eyeicon1');
const eyeicon2 = document.querySelector('#eyeicon2');
const eyeicon3 = document.querySelector('#eyeicon3');

function showandhidepassword(shpassword,eyeicon){
  if (shpassword.type === 'password') {
    shpassword.type = 'text';
    let staticimg = "/static/image/icons8-eye-30.png"
    eyeicon.src = staticimg;
    console.log(eyeicon.src)
  }
  else {
    shpassword.type = 'password';
    let staticimg = "/static/image/icons8-hide-30.png"
    eyeicon.src = staticimg;
  }
}

eyeicon1.addEventListener('click' , () => {
  showandhidepassword(logpassword,eyeicon1);
});

eyeicon2.addEventListener('click' , () => {
  showandhidepassword(signpassword,eyeicon2);
})

eyeicon3.addEventListener('click' , () => {
  showandhidepassword(signconfpassword,eyeicon3);
})



// Check for valid user 
const aname = document.querySelector('.account-name');
const name_check = aname.textContent;
if(name_check === 'invalid') {
  setTimeout(function(){
    alert('Invalid Username and Password!');
  },100);
  background.style.filter = 'blur(5px)';
  login.classList.add('active-login');
}
else if (name_check.indexOf(' ') >= 0) {
  const accountdiv = document.querySelector('.account-info');
  const login_button = document.querySelector('.login-button');
  accountdiv.classList.add('active-account');
  login_button.classList.add('active-button');
}
else if(name_check == 'incorrect'){
  setTimeout(function(){
    alert('Account Already Exists!');
  },100);
  background.style.filter = 'blur(5px)';
  signup.classList.add('active-signup');
  aname.textContent = 'None'
}



// on search button click check for sources and destination 
const searchbutton = document.querySelector(".search-button");
searchbutton.addEventListener('click', (event)=> {
  const from = document.querySelector('#from');
  const to = document.querySelector('#to');
  const dateInput = document.getElementById('travel-date');
  console.log(dateInput.value);
  if (from.value === 'Sources' || to.value === 'Destination'){
    event.preventDefault();
    alert('Please Select Source and Destination!');
  }
  else if (!dateInput.value){
    event.preventDefault();
    alert('Please Select date!');
  }
})



