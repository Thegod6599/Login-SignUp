# Flask Authentication Template

A simple authentication template built with Flask.  
Includes user signup, login, session handling, and logout.

## Features

- User signup with username, password, and email
- Secure password hashing
- Session-based authentication
- Protected dashboard route
- Logout system
- JSON-based user storage
- Frontend + backend separation

## Tech Stack

- Python
- Flask
- HTML
- CSS
- JavaScript
- Werkzeug Security


## Project Structure

.
├── main.py
├── users.json
├── templates
│   ├── index.html
│   └── dashboard.html
├── static
│   ├── style.css
│   └── static.js
├── .gitignore
└── README.md

## Setup Instructions

1. Clone the repository

git clone https://github.com/your-username/your-repo-name.git
cd your-repo-name

3. Install dependencies

pip install flask werkzeug

3. Set the secret key

Open `main.py` and set:
app.secret_key = "USE_YOUR_OWN_KEY"

4. Run the application

python main.py


6. Open in your browser:

http://localhost:5000

## Security Notes

- Passwords are hashed using Werkzeug
- `users.json` is for development/testing only
- Replace JSON storage with a database for production
- Always use a strong secret key

## Purpose

This project demonstrates:

- Authentication logic
- Session handling
- Secure password storage
- Flask routing
- Frontend and backend interaction

## License

MIT License