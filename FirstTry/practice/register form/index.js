const userName = document.getElementById("userName");
const passWord = document.getElementById("passWord");
const button = document.getElementById("mySubmit");
const myP1 = document.getElementById("myP1");
const myP2 = document.getElementById("myP2");
let min= 10;
let max = 110;
let generatedUser;
let generatedPass;
let user = Math.floor(Math.random()*max)+min;
console.log(user);

button.onclick = function(){
    userName = document.getElementById("userName").value.concat("@gmail.com");
    generatedUser = userName + user;
    myP1.textContent = `Your username is ${generatedUser}`;
    passWord  = document.getElementById("passWord").value;
    myP2.textContent = `Your password is: ${passWord}`;
}
