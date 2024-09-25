const decrease = document.getElementById(`decreaseBtn`);
const increase = document.getElementById(`increaseBtn`);
const reset = document.getElementById(`resetBtn`);
const countlabel = document.getElementById(`countLabel`);

let count = 0;

decrease.onclick = function(){
    count--;
    countlabel.textContent = count;
}
increase.onclick = function(){
    count++;
    countlabel.textContent = count;
}
reset.onclick = function(){
    count = 0;
    countlabel.textContent = count;
}