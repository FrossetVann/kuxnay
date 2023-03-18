if (document.documentElement.clientWidth > 431) {
  let nextBtn = document.getElementById('nextBtn');
  let prevBtn = document.getElementById('prevBtn');
  
  nextBtn.onclick = function()
  {
    let regImg = document.getElementById('img-bg');
    regImg.style.left = "0px";
   
  }
  prevBtn.onclick = function()
  {
    let regImg = document.getElementById('img-bg');
    regImg.style.left = "calc(100vw - 50vw)";
   
  }
} else {
  document.getElementById('nextBtn').onclick = function() {
    document.getElementById('reg-step2').classList.remove('registration-step2_nonvisibility');
    document.getElementById('reg-step1').classList.add('registration-step1_nonvisibility');
  }
  document.getElementById('prevBtn').onclick = function() {
    document.getElementById('reg-step2').classList.add('registration-step2_nonvisibility');
    document.getElementById('reg-step1').classList.remove('registration-step1_nonvisibility');
  }
};