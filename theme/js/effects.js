/* ICON MENU HAMBURGUER */

var iconMenu = document.querySelector('#icon-menu');

iconMenu.addEventListener('click', function(){
    document.querySelector('.overlay').style.display = "block";
    document.querySelector('#second-menu').style.display = "flex";
})

var iconCloseMenu = document.querySelector('#close-menu');

iconCloseMenu.addEventListener('click', function(){
    document.querySelector('#second-menu').style.display = "none";
    document.querySelector('.overlay').style.display = "none";
})