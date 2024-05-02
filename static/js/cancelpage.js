// Get all checkboxes
var checkboxes = document.querySelectorAll('input[type="checkbox"]');
let totalrefundamount = 0;
const perseatamount = parseInt(document.querySelector('.perseatamount').textContent);
const refunadamount = perseatamount * 60 / 100;
const refundableamountdiv = document.querySelector('.refundableamount');
const refunddiv = document.querySelector('.refund');
let checkedboxclick = 0;
let checkboxunclick = 0;
// let totalAmount = 0;

const updatedamount = document.querySelector('#updatedamount');
const urefundamount = document.querySelector('#urefundamount');

// Add event listener to each checkbox
checkboxes.forEach(function(checkbox) {
    checkbox.addEventListener('click', function() {
        let totalAmount = parseInt(document.querySelector('.totalAmount').textContent);
        if (checkbox.checked){
            totalrefundamount += refunadamount;
            totalAmount -= refunadamount;
            refundableamountdiv.textContent = Math.round(totalrefundamount);
            document.querySelector('.totalAmount').textContent = Math.round(totalAmount);
            updatedamount.value = Math.round(totalAmount);
            urefundamount.value = Math.round(totalrefundamount);
            refunddiv.classList.add('active');
            checkedboxclick++;
        }
        else {
            totalrefundamount -= refunadamount; 
            totalAmount += refunadamount;
            refundableamountdiv.textContent = Math.round(totalrefundamount);
            document.querySelector('.totalAmount').textContent = Math.round(totalAmount);
            updatedamount.value = Math.round(totalAmount);
            urefundamount.value = Math.round(totalrefundamount);
            checkboxunclick++;
            if (checkedboxclick == checkboxunclick){
                refunddiv.classList.remove('active');
            }
        }
    });
});
