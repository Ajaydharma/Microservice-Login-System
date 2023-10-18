from flask import Flask, Blueprint, render_template, request, redirect, url_for, session
from werkzeug.security import check_password_hash, generate_password_hash

auth_blueprint = Blueprint('auth', __name__)
app = Flask(__name__)

# A simple in-memory user database (not suitable for production).
users = {
    'user1': {'username': 'user1', 'password': generate_password_hash('password1')},
    'user2': {'username': 'user2', 'password': generate_password_hash('password2')}
}

# Check if the user is logged in.
def is_authenticated():
    return 'user' in session

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        user = users.get(username)

        if user and check_password_hash(user['password'], password):
            session['user'] = username
            return redirect(url_for('profile'))

        return 'Invalid username or password'

    return render_template('login.html')

@app.route('/logout')
def logout():
    session.pop('user', None)
    return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)