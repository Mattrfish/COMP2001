#app.py
from flask import Flask, request, jsonify, redirect, render_template, json
from flask_jwt_extended import JWTManager, create_access_token
import config, requests
from utils import role_required
from models import Trail, Features, User
from config import db

app = config.connex_app
flask_app = app.app
app.add_api(config.basedir / "swagger.yml")
AUTH_API_URL = "https://web.socem.plymouth.ac.uk/COMP2001/auth/api/users"

# Initialize JWTManager with the Flask app
jwt = JWTManager(flask_app)

@app.route("/")
def home():
    trails = Trail.query.all()
    features = Features.query.all()
    return render_template("home.html", trails=trails, features=features)


def authenticate_user(email, password):
    credentials = {"email": email, "password": password}
    try:
        response = requests.post(AUTH_API_URL, json=credentials)
        if response.status_code == 200:
            response_data = response.json()
            if response_data and response_data[1] == "True":
                user = User.query.filter_by(EmailAddress=email).first()
                if user:
                    return {"email": email, "role": user.Role, "id": user.UserID}
        return None
    except Exception as e:
        print(f"Error with authentication API: {e}")
        return None

@app.route("/swagger", methods=["POST"])
def swagger_ui():
    data = request.json
    email = data.get("email")
    password = data.get("password")

    if not email or not password:
        return jsonify({"message": "Email and password are required"}), 401

    user = authenticate_user(email, password)
    if user:
        access_token = create_access_token(identity=json.dumps(user))
        print(F"Access Token: {access_token}")
        redirect_url = f"http://localhost:8000/api/ui"
        print(f"Redirecting to: {redirect_url}")  # Debug log
        return jsonify({"access_token": access_token}), 200
    else:
        return jsonify({"message": "Invalid credentials"}), 403

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)
