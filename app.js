document.addEventListener("DOMContentLoaded", function () {
    function toggleMenu() {
        var menu = document.querySelector(".nav-menu");
        menu.classList.toggle("show");
      }
  });

  document.addEventListener("DOMContentLoaded", function() {
    var animation = lottie.loadAnimation({
      container: document.getElementById('email-animation'),
      renderer: 'svg',
      loop: true,
      autoplay: true,
      path: 'lotties/email-animation.json' // Replace with your file path
      

    });
    lottie.loadAnimation({
      container: document.getElementById('cold-email-animation'),
      renderer: 'svg',
      loop: true,
      autoplay: true,
      path: 'lotties/cold-email-automation-orange.json'
    });
  
    lottie.loadAnimation({
      container: document.getElementById('email-verification-animation'),
      renderer: 'svg',
      loop: true,
      autoplay: true,
      path: 'lotties/email-verification-orange.json'
    });
  });
  