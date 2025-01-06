#app.py
from flask import Flask, request, jsonify, redirect, render_template, json
from flask_jwt_extended import JWTManager, create_access_token
import config, requests
from models import Trail, Features, User
from config import db

# Initialize the Flask app using the Connexion framework
app = config.connex_app
flask_app = app.app

app.add_api(config.basedir / "swagger.yml")# Add api doc from swagger.yml config file
AUTH_API_URL = "https://web.socem.plymouth.ac.uk/COMP2001/auth/api/users" #url for auth api

# Initialize JWTManager with the Flask app for handling access tokens
jwt = JWTManager(flask_app)

#render homepage 
@app.route("/")
def home():
    trails = Trail.query.all()
    features = Features.query.all()
    return render_template("home.html", trails=trails, features=features)

# authenticate userwith api, then retrieve the user role from db 
def authenticate_user(email, password):
    credentials = {"email": email, "password": password}
    try:
        response = requests.post(AUTH_API_URL, json=credentials) #POST request to auth api
        if response.status_code == 200:
            response_data = response.json()
            if response_data and response_data[1] == "True": # verify successful auth
                user = User.query.filter_by(EmailAddress=email).first() #get user details from db using email
                if user:
                    return {"email": email, "role": user.Role, "id": user.UserID} # return user details
        return None
    except Exception as e:
        print(f"Error with authentication API: {e}")# error message
        return None

#hanlde login and return an access token for auth users
@app.route("/swagger", methods=["POST"])
def swagger_ui():
    data = request.json
    email = data.get("email")
    password = data.get("password")# get details from the request

    if not email or not password:
        return jsonify({"message": "Email and password are required"}), 401

    user = authenticate_user(email, password) # auth the user and retrieve the details
    if user:
        #create an access token for auth user
        access_token = create_access_token(identity=json.dumps(user))
        print(F"Access Token: {access_token}")
        redirect_url = f"http://localhost:8000/api/ui"
        print(F"Redirecting to: {redirect_url}")

        #return access token and ui url 
        return jsonify({"access_token": access_token, "redirect_url": redirect_url}), 200
    else:
        return jsonify({"message": "Invalid credentials"}), 403

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)
