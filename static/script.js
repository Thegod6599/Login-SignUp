function signUp() {
    const username = document.getElementById('su-username').value;
    const password = document.getElementById('su-password').value;
    fetch('/signup', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ username, password })
    })
    .then(res => res.json())
    .then(data => {
        if (data.ok) {
            alert('Sign up successful!');
        } else {
            alert('Sign up failed: ' + data.message);
        }
    })
    .catch(error => {
        console.error('Sign up error:', error);
        alert('Sign up error: ' + error.message);
    });

    // Clear the input fields
    document.getElementById('su-username').value = '';
    document.getElementById('su-password').value = '';
};

function login() {
    const username = document.getElementById('li-username').value;
    const password = document.getElementById('li-password').value;
    fetch('/login',{
          method: 'POST',
          headers: {
              'Content-Type': 'application/json'
          },
          body: JSON.stringify({ username, password })
    })
    .then(res => res.json())
    .then(data => {
        if (data.ok) {
            alert('Login successful!');
        } else {
            alert('Login failed: ' + data.message);
        }
    })
    .catch(error => {
        console.error('Login error:', error);
        alert('Login error: ' + error.message);
    });
    // Clear the input fields
    document.getElementById('li-username').value = '';
    document.getElementById('li-password').value = '';
};