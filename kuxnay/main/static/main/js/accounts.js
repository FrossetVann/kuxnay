let editBtn = document.getElementById('editBtn');
let exitBtn = document.getElementById('exitBtn');
let accountFirstName =document.getElementById('accountFirstName');
let accountLastName =document.getElementById('accountLastName');
let accountBithday =document.getElementById('bithday-date');
let accountInputFirstName=document.getElementById('accountInputFirstName');
let accountInputLastName=document.getElementById('accountInputLastName');
let accountInputBithday=document.getElementById('accBithday');
let imgChangelink=document.getElementById('imgChangelink');
let accountImage= document.getElementById('account-image');

editBtn.addEventListener('change', () => {

});
editBtn.addEventListener('click', () => {
  
  accountFirstName.classList.toggle('hidden');
  accountLastName.classList.toggle('hidden');
  accountBithday.classList.toggle('hidden');
  exitBtn.classList.toggle('hidden');
    imgChangelink.classList.toggle('hidden');
    let link=imgChangelink.value;
    accountImage.setAttribute('src', link );
  accountInputFirstName.classList.toggle('hidden');
  accountInputLastName.classList.toggle('hidden');
  accountInputBithday.classList.toggle('hidden');
  accountInputFirstName.classList.toggle('input-column');
  accountInputLastName.classList.toggle('input-column');
  accountFirstName.innerHTML=accountInputFirstName.value;
  accountLastName.innerHTML=accountInputLastName.value;
  accountBithday.innerHTML=accountInputBithday.value;

});

