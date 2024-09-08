// script.js
let hideMenuTimeout;

document.getElementById('hamburger-menu').addEventListener('click', function() {
    var navMenu = document.getElementById('nav-menu');
    navMenu.classList.toggle('show');
    
    if (navMenu.classList.contains('show')) {
        setHideMenuTimeout();
    }
});

document.getElementById('nav-menu').addEventListener('mouseenter', function() {
    clearTimeout(hideMenuTimeout);
});

document.getElementById('nav-menu').addEventListener('mouseleave', function() {
    setHideMenuTimeout();
});

function setHideMenuTimeout() {
    hideMenuTimeout = setTimeout(function() {
        document.getElementById('nav-menu').classList.remove('show');
    }, 8000); // 10000 milliseconds = 10 seconds
}