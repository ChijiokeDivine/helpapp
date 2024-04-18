$(document).ready(function(){
    $('#ContactForm').on('submit', function(e) {
        e.preventDefault();

        var fullName = $('#fullName').val();
        var email = $('#email').val();
        var message = $('#message').val();
        var errorMessage = $('#ContactErrorMessage');
        var isValid = true;

        // Validate full name
        if (fullName.trim() === '') {
            errorMessage.text('Please enter your full name.');
            isValid = false;
        }

        // Validate email address
        else if (email.trim() === '') {
            errorMessage.text('Please enter your email address.');
            isValid = false;
        } else if (!isValidEmailAddress(email)) {
            errorMessage.text('Please enter a valid email address.');
            isValid = false;
        }

        // Validate message
        else if (message.trim() === '') {
            errorMessage.text('Please enter your message or enquiry.');
            isValid = false;
        }

        if (isValid) {
            $('#contactSubmit').prop('disabled', true).html('<span class="spinner-border spinner-border-sm" role="status" aria-hidden="true"></span> Submitting...');

            $.ajax({
                type: 'POST',
                url: '/contact', 
                data: $(this).serialize(),
                success: function(response) {
                    if (response.success) {
                        
                        function showNotification() {
                            var notification = document.getElementById("notification");
                            notification.style.display = "block";
                            
                            setTimeout(function() {
                                notification.style.display = "none";
                            }, 3000); 
                        }
                        showNotification();
                      
                    } else {
                        // Submit failure
                        const errorObj = JSON.parse(response.errors);
                        const message = errorObj.message[0].message;
                        errorMessage.text(`${message} in the message field`);
                        setTimeout(() => {
                            errorMessage.text("");
                        }, 4000);
                    }
                },
                error: function(error) {
                    // Handle error
                },
                complete: function() {
                    $('#contactSubmit').prop('disabled', false).html('Submit');
                }
            });
        }
    });
});

function isValidEmailAddress(email) {
    // Regular expression for email validation
    var emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    return emailRegex.test(email);
}



const observer = new IntersectionObserver((entries) => {
    entries.forEach((entry) => {
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
        if (entry.isIntersecting){
            entry.target.classList.add('visible-link');
        }
       
    });
  });
const observ = new IntersectionObserver((entries) => {
    entries.forEach((entry) => {
        if (entry.isIntersecting){
            entry.target.classList.add('visible-link');
        }
       
    });
  });
const obser = new IntersectionObserver((entries) => {
    entries.forEach((entry) => {
  
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
  
  
  
  