//script de registro

document.getElementById('registerForm')?.addEventListener('submit', function(event) {
    event.preventDefault();

    const email = document.getElementById('registerEmail').value;
    const password = document.getElementById('registerPassword').value;

    if (email && password) {
     
        localStorage.setItem('userEmail', email);
        localStorage.setItem('userPassword', password);

       
        alert('Cuenta creada exitosamente');
        window.location.href = 'login.html';
    } else {
        alert('Por favor, complete todos los campos.');
    }
});



///scrip del downbar///
document.getElementById('userButton').addEventListener('click', function(event) {
    event.stopPropagation();
    document.getElementById('userDropdown').classList.toggle('active');
});

document.addEventListener('click', function(event) {
    const dropdown = document.getElementById('userDropdown');
    const button = document.getElementById('userButton');
    
    if (!dropdown.contains(event.target) && !button.contains(event.target)) {
        dropdown.classList.remove('active');
    }
});



//scrip barmenu

document.getElementById('userButton').addEventListener('click', function() {
    document.getElementById('userDropdown').classList.toggle('active');
});

// Close dropdown when clicking outside
document.addEventListener('click', function(event) {
    const dropdown = document.getElementById('userDropdown');
    const button = document.getElementById('userButton');
    
    if (!dropdown.contains(event.target) && !button.contains(event.target)) {
        dropdown.classList.remove('active');
    }
});