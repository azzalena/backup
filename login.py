from flask import Flask, render_template, request, redirect, url_for, session
import hashlib
import sqlite3

app = Flask(__name__)
app.secret_key = "secret_key" # Set secret key for session

# Connect to database
conn = sqlite3.connect('users.db')
c = conn.cursor()

# Create table to store user credentials
c.execute('''CREATE TABLE IF NOT EXISTS users
             (username TEXT PRIMARY KEY, password TEXT)''')
conn.commit()

# Registration form
@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        # Hash password before storing in database
        hashed_password = hashlib.sha256(password.encode('utf-8')).hexdigest()
        
        # Check if username already exists
        c.execute("SELECT * FROM users WHERE username=?", (username,))
        if c.fetchone() is not None:
            return "Username already exists"
        
        # Insert new user into database
        c.execute("INSERT INTO users VALUES (?, ?)", (username, hashed_password))
        conn.commit()
        
        return redirect(url_for('login'))
        
    return render_template('register.html')

# Login form
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        # Hash password before comparing with stored hash
        hashed_password = hashlib.sha256(password.encode('utf-8')).hexdigest()
        
        # Check if username and password match
        c.execute("SELECT * FROM users WHERE username=? AND password=?", (username, hashed_password))
        user = c.fetchone()
        if user is not None:
            session['username'] = user[0] # Start session
            return redirect(url_for('dashboard'))
        
        return "Invalid credentials"
        
    return render_template('login.html')

# Dashboard (requires authentication)
@app.route('/dashboard')
def dashboard():
    if 'username' not in session:
        return redirect(url_for('login'))
    
    return render_template('dashboard.html', username=session['username'])

# Logout
@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('login'))