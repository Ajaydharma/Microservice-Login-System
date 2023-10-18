from flask import Flask, Blueprint, render_template, session

profile_blueprint = Blueprint('profile', __name__)

app = Flask(__name__)  # Create the Flask application

@profile_blueprint.route('/profile')
def profile():
    if 'user' in session:
        username = session['user']
        return f'Welcome, {username}! This is your profile.'
    else:
        return 'You are not logged in.'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
