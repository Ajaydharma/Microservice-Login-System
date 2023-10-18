from flask import Flask

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Replace with a secure secret key.

# Import the login routes from login.py in the auth-service
from auth_service.login import auth_blueprint as auth
app.register_blueprint(auth, url_prefix='/auth')

# Import the profile routes from profile.py in the profile-service
from profile_service.profile import profile_blueprint as profile
app.register_blueprint(profile, url_prefix='/profile')

if __name__ == '__main__':
    app.run(debug=True)
