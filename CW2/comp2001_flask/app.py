from flask import Flask, request, jsonify, redirect, url_for, render_template
from flask_jwt_extended import JWTManager, jwt_required, get_jwt_identity
import config, requests
from models import Trail, Features

app = config.connex_app
app.add_api(config.basedir / "swagger.yml")
AUTH_API_URL = "https://web.socem.plymouth.ac.uk/COMP2001/auth/api/users"



def authenticate_user(email, password):
    credentials = {
        "email": email,  # Use the variable name here
        "password": password  # Use the variable name here
    }
    try:
        response = requests.post(AUTH_API_URL, json=credentials)
        if response.status_code == 200:
            # Assuming the Auth API returns a list
            response_data = response.json()
            if response_data and response_data[1] == "True":
                return True
        return False
    except Exception as e:
        print(f"Error with authentication API: {e}")
        return False

@app.route("/")
def home():
    trails = Trail.query.all()
    features = Features.query.all()
    return render_template("home.html", trails=trails, features=features)

# Route to handle Swagger UI authentication
@app.route("/swagger", methods=["POST"])

def swagger_ui():
    # Retrieve the email and password from the POST body
    data = request.json
    email = data.get("email")
    password = data.get("password")

    if not email or not password:
        return jsonify({"message": "Email and password are required"}), 401

    # Authenticate user via Authenticator API
    if authenticate_user(email, password):
        # If authentication is successful, redirect to Swagger UI
        return redirect("http://localhost:8000/api/ui")

    else:
        return jsonify({"message": "Invalid credentials"}), 403


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)
