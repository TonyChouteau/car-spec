$(document).ready(function() {
    // Form submission event
    $("#loginForm").submit(function(event) {
        // Prevent the form from submitting if validation fails
        if (!validateForm()) {
            event.preventDefault();
        }
    });

    // Client-side validation
    function validateForm() {
        var username = $("#username").val();
        var password = $("#password").val();

        // Check if username and password are not empty
        if (username === "" || password === "") {
            $("#error-message").text("Both fields are required.");
            return false;  // Prevent form submission
        }

        // Clear the error message if validation is successful
        $("#error-message").text("");
        return true;  // Allow form submission
    }
});
