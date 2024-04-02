$(document).ready(function () {
  // Nice Select Initialization
  // $('select').niceSelect();
  AOS.init({
    once: true,
    duration: 1000,
    disable: function () {
      var maxWidth = 991;
      return window.innerWidth < maxWidth;
    }
  });
  // Pricing Plan Change Trigger


});




$(window).on('load', function () {
  $("body").addClass("loading");
  setTimeout(function () {
    $(".preloader-wrapper").fadeOut(500);
    $("body").removeClass("loading");
  }, 1000);
  setTimeout(function () {
    $(".preloader-wrapper").remove();
  }, 2000);
});

//pagination

$(document).ready(function () {
  // change active class on pagination
  $('.pagination-wrapper').each(function (i, buttonGroup) {
    var $buttonGroup = $(buttonGroup);
    $buttonGroup.on('click', '.btn-main', function () {
      $buttonGroup.find('.active').removeClass('active');
      $(this).addClass('active');
    });
  });
});

$('#waitlistForm').on('submit', function(e) {
  e.preventDefault();
  
  // Disable the button and show loading state
  $('#waitlistBtn').prop('disabled', true).html('<span class="button-content"><span class="spinner-border spinner-border-sm" role="status" aria-hidden="true"></span> Joining...</span>');

  $.ajax({
      type: 'POST',
      url: '/waitlist/',  
      data: $(this).serialize(),
      success: function(response) {
          if (response.success) {
        
              window.location.href = '/success/';  
          } else {
              
            const errorObj = JSON.parse(response.errors);
                

            const message = errorObj.email[0].message;
              $("#waitErrorMessage").text(message);
              setTimeout(() => {
                  $("#waitErrorMessage").text("");
              }, 4000);
          }
      },
      error: function(error) {
          // Handle error
          console.log(error.responseText);
          
      },
      complete: function() {
          // Re-enable the button and restore its original text
          $('#waitlistBtn').prop('disabled', false).html('<span class="button-content">Join Waitlist</span>');
      }
  });
});


const observer = new IntersectionObserver((entries) => {
  entries.forEach((entry) => {
      console.log(entry)
      if (entry.isIntersecting){
          entry.target.classList.add('visible-link');
      }
      // else{
      //     entry.target.classList.remove('visible-link');
      // }
  });
});
const observerer = new IntersectionObserver((entries) => {
  entries.forEach((entry) => {
      console.log(entry)
      if (entry.isIntersecting){
          entry.target.classList.add('visible-link');
      }
     
  });
});
const observ = new IntersectionObserver((entries) => {
  entries.forEach((entry) => {
      console.log(entry)
      if (entry.isIntersecting){
          entry.target.classList.add('visible-link');
      }
     
  });
});
const obser = new IntersectionObserver((entries) => {
  entries.forEach((entry) => {
      console.log(entry)
      if (entry.isIntersecting){
          entry.target.classList.add('visible-link');
      }
     
  });
});

const hiddenElements = document.querySelectorAll("[show]");
hiddenElements.forEach((el) => observer.observe(el));
const hiddenElement = document.querySelectorAll("[see]");
hiddenElement.forEach((el) => observerer.observe(el));
const hiddenElemen = document.querySelectorAll("[goLeft]");
hiddenElemen.forEach((el) => observ.observe(el));

const hiddenEleme = document.querySelectorAll("[goRight]");
hiddenEleme.forEach((el) => obser.observe(el));