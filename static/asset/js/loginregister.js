const loginbtn = document.querySelector(".loginbtn");
const registerbtn = document.querySelector(".registerbtn");
let logincard = document.querySelector(".login-container");
let registercard = document.querySelector(".register-container");
const bg = document.querySelector(".bg-container")

loginbtn.addEventListener('click', function(){
    logincard.style.display = "flex";
    logincard.style.flexDirection = "column"
    logincard.style.alignItems = "center"
    loginbtn.style.display = "none";
    registerbtn.style.display = "none";
    bg.style.filter = "blur(4px)";
})

registerbtn.addEventListener('click', function(){
    loginbtn.style.display = "none";
    registerbtn.style.display = "none";
    registercard.style.display = "flex";
    registercard.style.flexDirection = "column";
    registercard.style.alignItems = "center";
    bg.style.filter = "blur(4px)";
})
