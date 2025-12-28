from flask import Flask, request, jsonify, render_template
from werkzeug.security import generate_password_hash, check_password_hash
import os, json

app = Flask(__name__)

# Create users.json file if it doesn't exist
if not os.path.exists('users.json'):
    with open('users.json', 'w') as f:
        json.dump({}, f)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/signup', methods=['POST'])
def signup():
    try:
        data = request.get_json()
        username = data.get('username', '').strip()
        password = data.get('password', '').strip()

        if not username or not password:
            return jsonify({
                "ok": False,
                'message': 'Username and password are required'
            })

        with open('users.json', 'r') as f:
            users = json.load(f)

        if username in users:
            return jsonify({"ok": False, 'message': 'User already exists'})

        hashed_password = generate_password_hash(password)
        users[username] = {"password": hashed_password}

        with open('users.json', 'w') as f:
            json.dump(users, f, indent=2)

        return jsonify({"ok": True, 'message': 'User created successfully'})
    except Exception as e:
        print(f"Error in signup: {e}")
        return jsonify({
            "ok": False,
            'message': f'Server error: {str(e)}'
        }), 500


@app.route('/login', methods=['POST'])
def login():
    try:
        data = request.get_json()
        username = data.get('username', '').strip()
        password = data.get('password', '').strip()

        with open('users.json', 'r') as f:
            users = json.load(f)

        if username in users and check_password_hash(users[username]["password"], password):
            return jsonify({"ok": True, 'message': 'Login successful'})
        else:
            return jsonify({
                "ok": False,
                'message': 'Invalid username or password'
            })
    except Exception as e:
        print(f"Error in login: {e}")
        return jsonify({
            "ok": False,
            'message': f'Server error: {str(e)}'
        }), 500


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
