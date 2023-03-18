document.getElementById('menu').onclick = function() {
    document.getElementById('menu').classList.toggle('menu_active');
    document.getElementById('header-nav').classList.toggle('header-nav_active');
    document.getElementById('logo').classList.toggle('logo_active');
    document.getElementById("myBodyID").classList.toggle('overflow_hidden');
  }