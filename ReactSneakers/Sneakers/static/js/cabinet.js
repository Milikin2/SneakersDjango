const userName = document.querySelector(".cabinet__data-name")// localStorage.cabinetName
const userLastname = document.querySelector(".cabinet__data-lastname")// localStorage.cabinetLastname
const userPhone= document.querySelector(".cabinet__data-phone")// localStorage.cabinetPhone
const userEmail = document.querySelector(".cabinet__data-email")// localStorage.cabinetEmail
const userLogin = document.querySelector(".cabinet__data-login")// localStorage.cabinetLogin
const userPassword = document.querySelector(".cabinet__data-password")// localStorage.cabinetPassword

userName.value = localStorage.cabinetName
userLastname.value = localStorage.cabinetLastname
userPhone.value = localStorage.cabinetPhone.slice(1, localStorage.cabinetPhone.lenght)
userEmail.value = localStorage.cabinetEmail
userLogin.value = localStorage.cabinetLogin
userPassword.value = localStorage.cabinetPassword