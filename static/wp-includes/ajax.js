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

    function showNotification() {
        var notification = document.getElementById("notification");
        notification.style.display = "block";
        
        setTimeout(function() {
            notification.style.display = "none";
        }, 3000); 
    }

    function isValidEmailAddress(email) {
        // Regular expression for email validation
        var emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
        return emailRegex.test(email);
    }

    // IntersectionObservers
    const observerOptions = {
        threshold: 0.1 // Adjust as needed
    };

    const handleIntersect = (entries) => {
        entries.forEach((entry) => {
            if (entry.isIntersecting) {
                entry.target.classList.add('visible-link');
            }
        });
    };

    const observer = new IntersectionObserver(handleIntersect, observerOptions);

    document.querySelectorAll("[show]").forEach((el) => observer.observe(el));
    document.querySelectorAll("[see]").forEach((el) => observer.observe(el));
    document.querySelectorAll("[goLeft]").forEach((el) => observer.observe(el));
    document.querySelectorAll("[goRight]").forEach((el) => observer.observe(el));
});
