let con = document.getElementsByClassName("slideshow-container");
let slideIndices = [];
const bus_containers = document.querySelectorAll(".bus-container");
// bus_containers.length;
for (let i = 1; i <= con.length; i++) {
    slideIndices.push(1);
    showSlides(slideIndices[0],i);
}
function plusSlides(n, slideshowIndex) {
    showSlides(slideIndices[slideshowIndex - 1] += n, slideshowIndex);
}

function showSlides(n, slideshowIndex) {
    let cont = document.querySelectorAll(".slideshow-container")[slideshowIndex - 1];
    let slides = cont.querySelectorAll(".bus-image");

    if (n > slides.length) {
        slideIndices[slideshowIndex - 1] = 1;
    }
    if (n < 1) {
        slideIndices[slideshowIndex - 1] = slides.length;
    }

    for (let i = 0; i < slides.length; i++) {
        slides[i].style.display = "none";
    }
    slides[slideIndices[slideshowIndex - 1] - 1].style.display = "block";
}



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


