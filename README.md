# Secure Coding Review: Python Flask Login Portal

## Overview
This repository contains a manual code review of a Python Flask application. The audit identifies critical security vulnerabilities in the authentication flow and provides remediated code based on secure coding best practices[cite: 4].

## Identified Vulnerabilities & Findings

**1. SQL Injection (SQLi)**
* **Finding:** The application constructs SQL queries using Python f-strings, directly concatenating user input into the execution string.
* **Risk:** An attacker can input `' OR '1'='1` as the username to bypass authentication or extract sensitive database tables.

**2. Hardcoded Secrets**
* **Finding:** The Flask `secret_key` is hardcoded directly into the source code in plaintext.
* **Risk:** If the source code is exposed or pushed to a public repository, attackers can forge session cookies and hijack user sessions.

**3. Plaintext Passwords**
* **Finding:** The system queries passwords in plaintext, implying passwords are not hashed in the database.
* **Risk:** A database breach immediately exposes all user passwords.

**4. Reflected Cross-Site Scripting (XSS)**
* **Finding:** The application returns the `username` input directly within HTML tags `<h1>` without sanitization.
* **Risk:** Attackers can inject malicious JavaScript payloads into the username field, which executes in the victim's browser.

## Remediation Steps & Best Practices

1. **Parameterize SQL Queries:** Use prepared statements (`?` placeholders in SQLite) instead of string concatenation to separate SQL logic from user data[cite: 4].
2. **Environment Variables:** Move all secrets, API keys, and configuration variables to a `.env` file that is excluded from version control[cite: 4].
3. **Cryptographic Hashing:** Implement strong, salted password hashing algorithms like Bcrypt or Argon2 for storing and verifying credentials[cite: 4].
4. **Input Sanitization:** Use template engines (like Flask's Jinja2) which automatically escape HTML context, or explicitly sanitize input before rendering[cite: 4].