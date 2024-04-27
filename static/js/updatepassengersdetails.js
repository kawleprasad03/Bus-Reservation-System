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
