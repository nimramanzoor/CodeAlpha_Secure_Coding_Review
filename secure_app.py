import sqlite3
import os
from flask import Flask, request, escape
from werkzeug.security import check_password_hash

app = Flask(__name__)
# REMEDIATION 1: Use environment variables for secrets
app.secret_key = os.environ.get("FLASK_SECRET_KEY", "default-dev-key")

@app.route('/login', methods=['POST'])
def login():
    username = request.form.get('username')
    password = request.form.get('password')
    
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    
    # REMEDIATION 2: Parameterized query prevents SQL Injection
    # REMEDIATION 3: Only fetch the hash, don't check plaintext passwords
    query = "SELECT password_hash FROM users WHERE username = ?"
    cursor.execute(query, (username,))
    result = cursor.fetchone()
    
    # REMEDIATION 3 (cont): Secure password verification
    if result and check_password_hash(result[0], password):
        # REMEDIATION 4: Escape user input to prevent XSS
        safe_username = escape(username)
        return f"<h1>Welcome back, {safe_username}!</h1>"
    else:
        return "Invalid credentials."

if __name__ == '__main__':
    app.run(debug=False) # Debug mode disabled for production