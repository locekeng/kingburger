// document.getElementById('login-toggle').addEventListener('click', function() {
//     document.getElementById('login-form').classList.remove('hidden');
//     document.getElementById('signup-form').classList.add('hidden');
//     document.getElementById('login-toggle').classList.add('active');
//     document.getElementById('signup-toggle').classList.remove('active');
// });

// document.getElementById('signup-toggle').addEventListener('click', function() {
//     document.getElementById('signup-form').classList.remove('hidden');
//     document.getElementById('login-form').classList.add('hidden');
//     document.getElementById('signup-toggle').classList.add('active');
//     document.getElementById('login-toggle').classList.remove('active');
// });


document.addEventListener('DOMContentLoaded', function () {
    const loginToggle = document.getElementById('login-toggle');
    const signupToggle = document.getElementById('signup-toggle');
    const loginForm = document.getElementById('login-form');
    const signupForm = document.getElementById('signup-form');

    loginToggle.addEventListener('click', function () {
        loginForm.classList.remove('hidden');
        signupForm.classList.add('hidden');
        loginToggle.classList.add('active');
        signupToggle.classList.remove('active');
    });

    signupToggle.addEventListener('click', function () {
        signupForm.classList.remove('hidden');
        loginForm.classList.add('hidden');
        signupToggle.classList.add('active');
        loginToggle.classList.remove('active');
    });
});