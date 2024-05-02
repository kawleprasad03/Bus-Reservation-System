 // Function to generate seats
 let nmbookedcheck = 0;
 let acbookedcheck = 0;
 let acseatnumberlist = [];
 let nmseatnumberlist = [];
 let allseatnumberlist = [];
 const amountdiv = document.querySelector('.amount');
 const seconddiv = (amountdiv.getElementsByTagName('div')[1]).getElementsByTagName('span')[1];
 const price = parseInt(seconddiv.textContent); 
 let totalPrice = price;
 console.log(price);
 console.log(typeof(price));

 function generateSeats(start, end, rowId) {
    let seats = "";
    for (let i = start; i <= end; i+=4) {
      seats += `<div class="seat available" id="seatS${i}" onclick="bookSeat(${i})">${i}</div>`;
    }
    document.getElementById(rowId).innerHTML = seats;
  }

  // Function to book a seat
  function bookSeat(seatNum) {
    let seat = document.getElementById(`seatS${seatNum}`);
    console.log(seat);
    if (nmbookedcheck >= 5){
      if (seat.classList.contains('available')){
        alert('Only booked 5 seats at a times!');
      }
      else{
        seat.classList.add('available');
        nmbookedcheck--;
        nmseatnumberlist = nmseatnumberlist.filter(item => item !== seat.textContent);
        totalPrice = totalPrice - price;
        seconddiv.textContent = totalPrice;
      }
    }
    else{
      if (seat.classList.contains('available')) {
        seat.classList.remove('available');
        seat.classList.add('booked');
        nmbookedcheck++;
        nmseatnumberlist.push(seat.textContent);
        if (nmbookedcheck == 1){
          amountdiv.style.display = "flex";
        }
        else{
          totalPrice = totalPrice + price;
          seconddiv.textContent = totalPrice;
        }
      } else {
        seat.classList.add('available');
        nmbookedcheck--;
        nmseatnumberlist = nmseatnumberlist.filter(item => item !== seat.textContent);
        if (nmbookedcheck == 0){
          amountdiv.style.display = "none";
        }
        else {
          totalPrice = totalPrice - price;
          seconddiv.textContent = totalPrice;
        }
      }
    }
  }

  // Generate seats for each row
  generateSeats(4, 40, 'row1');
  generateSeats(3, 40, 'row2');
  generateSeats(2, 40, 'row3');
  generateSeats(1, 40, 'row4');



    // Function to generate ACseats
    function ACgenerateSeats(start, end, ACrowId) {
      let seats = "";
      let inc = 0;
      if (ACrowId=="ACrow4" || ACrowId=="ACrow5" || ACrowId=="ACrow6"){
        inc = 3;
      }
      else {
        inc = 4;
      }
      for (let i = start; i <= end; i+=inc) {
        seats += `<div class="ACseat available" id="ACseatA${i}" onclick="ACbookSeat(${i})">${i}</div>`;
      }
      document.getElementById(ACrowId).innerHTML = seats;
    }

    // Function to book a seat
    function ACbookSeat(seatNum) {
      let seat = document.getElementById(`ACseatA${seatNum}`);
      // console.log(seat);
      if (acbookedcheck >= 5) {
        if (seat.classList.contains('available')){
          alert('Only booked 5 seats at a times!');
        }
        else{
          seat.classList.add('available');
          acbookedcheck--;
          acseatnumberlist = acseatnumberlist.filter(item => item !== seat.textContent);
          totalPrice = totalPrice - price;
          seconddiv.textContent = totalPrice;
        } 
      }
      else {
        if (seat.classList.contains('available')) {
          seat.classList.remove('available');
          seat.classList.add('booked');
          acbookedcheck++;
          acseatnumberlist.push(seat.textContent);
          if (acbookedcheck == 1){
            amountdiv.style.display = "flex";
          }
          else{
            totalPrice = totalPrice + price;
            seconddiv.textContent = totalPrice;
          }
        } else {
          seat.classList.add('available');
          acbookedcheck--;
          acseatnumberlist = acseatnumberlist.filter(item => item !== seat.textContent);
          if (acbookedcheck == 0){
            amountdiv.style.display = "none";
          }
          else {
            totalPrice = totalPrice - price;
            seconddiv.textContent = totalPrice;
          }
        }
      }
    }

    // Generate ACseats for each row
    ACgenerateSeats(3, 31, 'ACrow1');
    ACgenerateSeats(2, 31, 'ACrow2');
    ACgenerateSeats(1, 31, 'ACrow3');
    ACgenerateSeats(34, 55, 'ACrow4');
    ACgenerateSeats(33, 55, 'ACrow5');
    ACgenerateSeats(32, 55, 'ACrow6');

    // if AC sleeper or seater that show by below code
    const typeofbus = document.querySelector('.checktypeofbus');
    const ACTypeSeating = document.querySelector('.ACseatsbus');
    const SeaterTypeSeating = document.querySelector('#seats');
    let bookedseats = document.querySelector('.allbookedseat').textContent;
    console.log(typeofbus.innerHTML);
    if(typeofbus.innerHTML == "yes"){
      SeaterTypeSeating.style.display = "none";
      ACTypeSeating.style.display = "block";
      // Remove leading and trailing whitespace and square brackets
      bookedseats = bookedseats.trim().slice(1, -1);

      // Convert the string to an array
      var bookedSeatsArray = bookedseats.split(',').map(function(item) {
        return item.trim().replace(/'/g, ''); // Remove single quotes
      });
      // console.log(bookedSeatsArray[0].length);
      if (bookedSeatsArray[0].length != 0){
        bookedSeatsArray.forEach(function(seat) {
          let blockseatno = document.querySelector('#ACseat'+seat);
          blockseatno.style.backgroundColor = '#26282A';
          blockseatno.onclick = null;
        });
      }
    }
    else{
      bookedseats = bookedseats.trim().slice(1, -1);
      // Convert the string to an array
      var bookedSeatsArray = bookedseats.split(',').map(function(item) {
        return item.trim().replace(/'/g, ''); // Remove single quotes
      });
      // console.log(bookedSeatsArray);
      if (bookedSeatsArray[0].length != 0){
        bookedSeatsArray.forEach(function(seat) {
          let blockseatno = document.querySelector('#seat'+seat);
          blockseatno.style.backgroundColor = '#26282A';
          blockseatno.onclick = null;
        });
      }
    }



  //boarding and dropping javascript
  // Function to toggle the visibility of options when header is clicked
  function toggleOptions(headerId, optionsId) {
  const options = document.getElementById(optionsId);
  const border = document.getElementById(headerId);
  options.classList.add('active');
  border.classList.add('active');

  // Hide other options if visible
  const allOptions = document.querySelectorAll('.options');
  allOptions.forEach((option) => {
      if (option.id !== optionsId && option.classList.contains('active')) {
      option.classList.remove('active');
      }
  });
  }

  toggleOptions('boardingHeader', 'boardingOptions');
  // Event listeners to toggle options on header click
  document.getElementById('boardingHeader').addEventListener('click', function() {
  document.getElementById('droppingHeader').classList.remove('active')
  toggleOptions('boardingHeader', 'boardingOptions');
  });

  document.getElementById('droppingHeader').addEventListener('click', function() {
    document.getElementById('boardingHeader').classList.remove('active')
  toggleOptions('droppingHeader', 'droppingOptions');
  });

  const maindiv = document.querySelector('.inner-details');
    // Function to generate the Passengerform 
  function generateForm(passengerNumber, seatNumber) {
    // Create elements
    var innerBox = document.createElement('div');
    innerBox.className = 'inner-box';

    var formGroup1 = document.createElement('div');
    formGroup1.className = 'form-group1';

    var h3 = document.createElement('h3');
    h3.className = 'subheading';
    h3.textContent = 'Passenger ' + passengerNumber + ' | Seat ' + seatNumber;

    var inputHiddenSeatNo = document.createElement('input');
    inputHiddenSeatNo.type = 'hidden';
    inputHiddenSeatNo.required = true;
    inputHiddenSeatNo.name = 'AllPassengerSeatNO';
    inputHiddenSeatNo.value = seatNumber;


    var hr = document.createElement('hr');

    var labelName = document.createElement('label');
    labelName.setAttribute('for', 'passengerName');
    labelName.className = 'passenger-label';
    labelName.textContent = 'Name';

    var inputName = document.createElement('input');
    inputName.type = 'text';
    inputName.className = 'passengerName';
    inputName.placeholder = 'Enter Name';
    inputName.required = true;
    inputName.name = 'Pname';

    // Append elements to formGroup1
    formGroup1.appendChild(h3);
    formGroup1.appendChild(inputHiddenSeatNo);
    formGroup1.appendChild(hr);
    formGroup1.appendChild(labelName);
    formGroup1.appendChild(inputName);

    // Create elements for formGroup2
    var formGroup2 = document.createElement('div');
    formGroup2.className = 'form-group2';

    var genderSelect = document.createElement('div');
    genderSelect.className = 'gender-select';

    var labelGender = document.createElement('label');
    labelGender.setAttribute('for', 'gender');
    labelGender.className = 'passenger-label';
    labelGender.textContent = 'Gender';

    var selectGender = document.createElement('select');
    selectGender.className = 'gender';
    selectGender.required = true;
    selectGender.name = 'Pgender';

    var optionDefault = document.createElement('option');
    optionDefault.value = 'select';
    optionDefault.selected = true;
    optionDefault.hidden = true;
    optionDefault.disabled = true;
    optionDefault.textContent = 'Select';

    var optionMale = document.createElement('option');
    optionMale.value = 'male';
    optionMale.textContent = 'Male';

    var optionFemale = document.createElement('option');
    optionFemale.value = 'female';
    optionFemale.textContent = 'Female';

    // Append elements to selectGender
    selectGender.appendChild(optionDefault);
    selectGender.appendChild(optionMale);
    selectGender.appendChild(optionFemale);

    // Append elements to genderSelect
    genderSelect.appendChild(labelGender);
    genderSelect.appendChild(selectGender);

    var ageDiv = document.createElement('div');
    ageDiv.className = 'age';

    var labelAge = document.createElement('label');
    labelAge.setAttribute('for', 'passengerAge');
    labelAge.className = 'passenger-label';
    labelAge.textContent = 'Age';

    var inputAge = document.createElement('input');
    inputAge.type = 'number';
    inputAge.className = 'passengerAge';
    inputAge.placeholder = 'Enter Age';
    inputAge.required = true;
    inputAge.name = 'Page';

    // Append elements to ageDiv
    ageDiv.appendChild(labelAge);
    ageDiv.appendChild(inputAge);

    // Append genderSelect and ageDiv to formGroup2
    formGroup2.appendChild(genderSelect);
    formGroup2.appendChild(ageDiv);

  
    // Append formGroup1, formGroup2, and formGroup3 to innerBox
    innerBox.appendChild(formGroup1);
    innerBox.appendChild(formGroup2);
  
    maindiv.appendChild(innerBox);
    var lineBreak = document.createElement('br');

    maindiv.appendChild(lineBreak);
  }

  // Example usage
  // generateForm(1, 'S01');

  
  // check for boarding radio button is checed or not
  function boardingcheck() {
    var radioButtons = document.getElementsByName('boarding');

    // Check if at least one radio button is checked
    for (var i = 0; i < radioButtons.length; i++) {
        if (radioButtons[i].checked) {
            return false; 
        }
    }

    return true;
  }

  // check for dropping radio button is checed or not
  function droppingcheck() {
    var radioButtons = document.getElementsByName('dropping');

    // Check if at least one radio button is checked
    for (var i = 0; i < radioButtons.length; i++) {
        if (radioButtons[i].checked) {
            return false; 
        }
    }

    return true;
  }


  // continue will display passenger form
  const continuebutton = document.querySelector('#continue');
  const background = document.querySelector('.background');
  const passengerform = document.querySelector('.passenger-details');
  const signup = document.querySelector('.signup');
  const ACprefix = "A"
  const Seaterprefix = "S"
  const innerdetails = document.querySelector('.inner-details');
  const TotalAmountSpan = document.querySelector('#TotalAmount'); 
  continuebutton.addEventListener('click' , () => {
    // sign up page will open when account-check is none
    const account_check = document.querySelector('.account-check').innerHTML;
    if (account_check == "None" || account_check == "incorrect") {
      background.style.filter = 'blur(5px)';
      signup.classList.add('active-signup');
    }
    else if(acbookedcheck == 0 && nmbookedcheck == 0) {
      alert("Please Select Seat First!");
    }
    else if(boardingcheck()) {
      // Display an alert if no radio button is checked
      alert("Please select a boarding option!");
    }
    else if(droppingcheck()) {
      // Display an alert if no radio button is checked
      alert("Please select a dropping option!");
    }
    else{
      background.style.filter = 'blur(5px)';
      passengerform.classList.add('active');
      TotalAmountSpan.textContent = totalPrice;
      document.querySelector('#TravelTotalAmount').value = totalPrice;
      if(typeofbus.innerHTML == "yes") {
        innerdetails.innerHTML = "";
        for (let i = 1; i <= acbookedcheck;i++){
          // allseatnumberlist.push(ACprefix + acseatnumberlist[i-1]);
          generateForm(i, ACprefix + acseatnumberlist[i-1]);
        }
        // document.querySelector('#AllPassengerSeatNO').value = AllPassengerSeatNO.toString();
        validatePassengerform();
      }
      else {
        innerdetails.innerHTML = "";
        for (let i = 1; i <= nmbookedcheck;i++){
          // AllPassengerSeatNO.push(Seaterprefix + nmseatnumberlist[i-1]);
          generateForm(i, Seaterprefix + nmseatnumberlist[i-1]);
        }
        // document.querySelector('#AllPassengerSeatNO').value = AllPassengerSeatNO.toString();
        validatePassengerform();
      }
    }
  })

  // close passenger form 
  const close = document.querySelector('.close');
  close.addEventListener('click' , () => {
    event.preventDefault();
    background.style.filter = 'blur(0px)';
    passengerform.classList.remove('active');
  })

  // close signup form
  const close2 = document.querySelector('.close2');
  close2.addEventListener('click' , (event) => {
    background.style.filter = 'blur(0)';
    signup.classList.remove('active-signup');
  })

  function validatePassengerform(){

  // name field take only character
  const passengernames = document.querySelectorAll('.passengerName');
  // console.log(passengernames)
  passengernames.forEach(function(passengername){
    passengername.addEventListener('input' , ()=> {
      let passengernamevalue = passengername.value;
      let alphvalue = passengernamevalue.replace(/[^a-zA-Z\s]/g,'');
      passengername.value = alphvalue;
    })
  })

  // age field take only digits and not greater than 100
  const passengerages = document.querySelectorAll('.passengerAge');
  // console.log(passengerages);
  passengerages.forEach(function(passengerage){
    passengerage.addEventListener('input' , () => {
      let passengeragevalue = passengerage.value;
      let numericvalue = passengeragevalue.replace(/\D/g,'');
      passengerage.value = numericvalue;
      if (passengerage.value > 100){
        alert('Please provide valid age!');
        passengerage.value = '';
      }
    })
  })
  
  // city field take only characters
  // const city = document.querySelector('#cityname');
  // console.log(city);
  // city.addEventListener('input' , () => {
  //   let cityvalue = city.value;
  //   let alphvalue = cityvalue.replace(/[^a-zA-Z]/g,'');
  //   city.value = alphvalue;
  // })
  }
  // Email validation
  const email1 = document.querySelector('#email1');
  email1.addEventListener('focusout', () => {
    const emailcheck = email1.value;
    const emailpattern = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    if (!emailpattern.test(emailcheck)){
      alert('Please enter a valid email address!');
    }
  }) 

  // Phone Number not more than 10 digits and only take digits
  const phone1 = document.querySelector('#phone_no');
  phone1.addEventListener('input', () => {
    const phonevalue = phone1.value;
    const numericvalue = phonevalue.replace(/\D/g,'');
    phone1.value = numericvalue;
    if (phone1.value.length > 10){
      phone1.value = phone1.value.slice(0,10);
    }
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
  const email = document.querySelector('#email2');
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


  eyeicon2.addEventListener('click' , () => {
    showandhidepassword(signpassword,eyeicon2);
  })

  eyeicon3.addEventListener('click' , () => {
    showandhidepassword(signconfpassword,eyeicon3);
  })

  // Check for valid user 
  // if(name_check === 'invalid') {
    //   setTimeout(function(){
      //     alert('Invalid Username and Password!');
      //   },100);
      //   background.style.filter = 'blur(5px)';
      //   login.classList.add('active-login');
      // }
      // if (name_check.indexOf(' ') >= 0) {
        //   setTimeout(function(){
          //         alert('Invalid Username and Password!');
          //       },100);
          // }



  const aname = document.querySelector('.account-check');
  const name_check = aname.innerHTML;
  if(name_check == 'incorrect'){
    setTimeout(function(){
      alert('Account Already Exists!');
    },100); 
    background.style.filter = 'blur(5px)';
    signup.classList.add('active-signup');
    aname.textContent = 'None';
  }


          


// payment form show 
const proceedButton = document.querySelector('#proceed');
const paymentdiv = document.querySelector('.card.box2');
proceedButton.addEventListener('click', () => {
  let checkpassengername = document.querySelectorAll(".passengerName");
  let checkpassengerage = document.querySelectorAll(".passengerAge");
  let checkpassengergender = document.querySelectorAll(".gender");
  let checkflag = true;
  // Loop through all passenger ages
  checkpassengername.forEach(function(input) {
    if (input.value === '') {
        checkflag = false;
        // alert("Please enter all passenger names!");
        return;
    }
  });

  // Loop through all passenger ages
  checkpassengerage.forEach(function(input) {
    if (input.value === '') {
        checkflag = false;
        // alert("Please enter all passenger ages!");
        return;
    }
  });

  // Loop through all passenger genders
  checkpassengergender.forEach(function(input) {
    if (input.value === 'select') {
        checkflag = false;
        // alert("Please select a gender for all passengers!");
        return;
    }
  });
  if(checkflag) {
    window.scrollTo({ top: 0, behavior: 'smooth' });
    background.style.filter = 'blur(5px)';
    console.log('proceed click');
    paymentdiv.classList.add('active');
  }
  else {
    alert("Please Submit Passengers Details!");
  }
})

// close payment form 
const close3 = document.querySelector('.close3');
close3.addEventListener('click' , () => {
  event.preventDefault(); 
  background.style.filter = 'blur(0px)';
  paymentdiv.classList.remove('active');

})

const bycash = document.querySelector("#bycash");
const creaditnav = document.querySelector("#creaditnav");
const paybutton = document.querySelector("#paybutton");
let inputWith = document.querySelector("#credit");
let colmd6 = document.querySelector("#code");
let colmd = document.querySelector("#experi");
let checkpaymentstatus = document.querySelector("#checkpaymentstatus");
checkpaymentstatus.value = 'Successful';

bycash.addEventListener("click", ()=> {
  inputWith.style.display = "none";
  colmd6.style.display = "none";
  colmd.style.display = "none";
  paybutton.textContent = "Continue";
  checkpaymentstatus.value = 'Pending';
  console.log(checkpaymentstatus.value);
})

creaditnav.addEventListener("click", () => {
  inputWith.style.display = "block";
  colmd6.style.display = "block";
  colmd.style.display = "block";
  paybutton.textContent = "Pay";
  checkpaymentstatus.value = 'Successful';
})

// const paymentorderid = document.querySelector('#paymentorderid').value;
// const paymentamount = document.querySelector('#paymentamount').value;
// console.log(paymentorderid);
// console.log(paymentamount)
// console.log(parseInt(paymentamount))
// console.log(typeof(parseInt(paymentamount)))
// var options = {
//   "key": "rzp_test_9r0bCNJPmdUai0", // Enter the Key ID generated from the Dashboard
//   "amount": parseInt(paymentamount), // Amount is in currency subunits. Default currency is INR. Hence, 50000 refers to 50000 paise
//   "currency": "INR",
//   "name": "Acme Corp",
//   "description": "Purchases Transaction",
//   "image": "https://example.com/your_logo",
//   "order_id": paymentorderid, //This is a sample Order ID. Pass the `id` obtained in the response of Step 1
//   "handler": function (response){
//       // alert(response.razorpay_payment_id);
//       // alert(response.razorpay_order_id);
//       // alert(response.razorpay_signature)
//       console.log(response);
//       alert("payment Sucsseful");
//   },
//   "prefill": {
//       "name": "Gaurav Kumar",
//       "email": "gaurav.kumar@example.com",
//       "contact": "9000090000"
//   },
//   // "notes": {
//   //     "address": "Razorpay Corporate Office"
//   // },
//   "theme": {
//       "color": "#3399cc"
//   }
// };
// var rzp1 = new Razorpay(options);
// rzp1.on('payment.failed', function (response){
//       alert(response.error.code);
//       // alert(response.error.description);
//       // alert(response.error.source);
//       // alert(response.error.step);
//       // alert(response.error.reason);
//       // alert(response.error.metadata.order_id);
//       // alert(response.error.metadata.payment_id);
// });
// document.getElementById('rzp-button1').onclick = function(e){
//   rzp1.open();
//   e.preventDefault();
// };
