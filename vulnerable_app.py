import sqlite3
from flask import Flask, request

app = Flask(__name__)
# VULNERABILITY 1: Hardcoded credentials/secrets
app.secret_key = "super_secret_production_key_123" 

@app.route('/login', methods=['POST'])
def login():
    username = request.form.get('username')
    password = request.form.get('password')
    
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    
    # VULNERABILITY 2: SQL Injection (SQLi)
    # VULNERABILITY 3: Plaintext password checking
    query = f"SELECT * FROM users WHERE username = '{username}' AND password = '{password}'"
    cursor.execute(query)
    user = cursor.fetchone()
    
    if user:
        # VULNERABILITY 4: Cross-Site Scripting (XSS)
        return f"<h1>Welcome back, {username}!</h1>"
    else:
        return "Invalid credentials."

if __name__ == '__main__':
    app.run(debug=True)