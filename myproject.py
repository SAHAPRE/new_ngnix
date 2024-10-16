from flask import Flask, request, jsonify, render_template, redirect, url_for, session

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Change this to a random secret key

# In-memory storage for users (username: password)
users = {}

@app.route("/")
def hello():
    return "<h1 style='color:red'>Hello There, what are you doing!</h1>"

@app.route("/signup", methods=["GET", "POST"])
def signup():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        
        if username in users:
            return "Username already exists!", 400
        
        users[username] = password  # In a real app, hash the password
        return "Signup successful!", 201
        
    return '''
        <form method="post">
            Username: <input type="text" name="username"><br>
            Password: <input type="password" name="password"><br>
            <input type="submit" value="Sign Up">
        </form>
    '''

@app.route("/signin", methods=["GET", "POST"])
def signin():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        
        if users.get(username) == password:  # In a real app, hash the password
            session['username'] = username
            return f"Welcome, {username}!"
        else:
            return "Invalid credentials!", 403
    
    return '''
        <form method="post">
            Username: <input type="text" name="username"><br>
            Password: <input type="password" name="password"><br>
            <input type="submit" value="Sign In">
        </form>
    '''

@app.route("/logout")
def logout():
    session.pop('username', None)
    return redirect(url_for('hello'))

if __name__ == "__main__":
    app.run(host='0.0.0.0')


