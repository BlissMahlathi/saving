const sub = document.getElementById(`myCheckBox`);
const visa = document.getElementById(`visaBtn`);
const mastercard =  document.getElementById(`masterCardBtn`);
const paypal = document.getElementById(`payPalBtn`);
const pSub = document.getElementById(`myP`);
const pPay = document.getElementById(`myP1`);
const button = document.getElementById(`myButton`);


button.onclick = function(){
    if(sub.checked){
        pSub.textContent = `You are Subscribed`;
       
    }
    else{
        pSub.textContent = ` You are not Subscribed`;
    }
    if(visa.checked){
        pPay.textContent = `You are paying with Visa`;
    }
    else if(mastercard.checked){
        pPay.textContent = `You are paying with Mastercard`;
    }
    else if(paypal.checked){
        pPay.textContent = `You are paying with PayPal`;
    }
    else{
        pPay.textContent = `Select a payment method`;
    }
}