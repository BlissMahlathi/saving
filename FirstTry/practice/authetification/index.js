const label = document.getElementById(`myLabel`);
const button =  document.getElementById(`mySubmit`);
const myP = document.getElementById(`myP`);
let text;

button.onclick = function(){
    text = document.getElementById(`text`).value;
    text = Number(text);
    if(text >= 50){
        myP.textContent = `You are too old to enter this site`;
    }
    else if(text >= 18){
        myP.textContent = `You are old enough to enter this site`;
    }
    else if(text == 0){
        myP.textContent = `You haven't been born yet`;
    }
    else if(text < 18){
        myP.textContent = `You are ${text} you can not enter this site`;
    }
}