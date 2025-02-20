from flask import Flask, jsonify, request
from flask_httpauth import HTTPBasicAuth
from werkzeug.security import generate_password_hash, check_password_hash
from flask_jwt_extended import JWTManager, jwt_required, create_access_token, get_jwt_identity

# Initialisations
app = Flask(__name__)
auth = HTTPBasicAuth()
jwt = JWTManager(app)

# Clé secrète pour les tokens JWT (modifiez cela pour une vraie clé secrète)
app.config['JWT_SECRET_KEY'] = 'votre_clé_secrète_pour_jwt'

# Utilisateurs en mémoire (dictionnaire)
users = {
    "user1": {"username": "user1", "password": generate_password_hash("password"), "role": "user"},
    "admin1": {"username": "admin1", "password": generate_password_hash("password"), "role": "admin"}
}

# Authentification de base avec Flask-HTTPAuth
@auth.verify_password
def verify_password(username, password):
    user = users.get(username)
    if user and check_password_hash(user['password'], password):
        return username

# Route protégée avec authentification de base
@app.route('/basic-protected', methods=['GET'])
@auth.login_required
def basic_protected():
    return "Basic Auth: Access Granted"

# Authentification par JWT
@app.route('/login', methods=['POST'])
def login():
    """Génère un token JWT si les identifiants sont valides"""
    username = request.json.get('username', None)
    password = request.json.get('password', None)
    user = users.get(username)

    if user and check_password_hash(user['password'], password):
        # Crée le token JWT avec l'identité de l'utilisateur
        access_token = create_access_token(identity=username)
        return jsonify(access_token=access_token)

    return jsonify({"error": "Identifiants invalides"}), 401

# Route protégée par JWT
@app.route('/jwt-protected', methods=['GET'])
@jwt_required()
def jwt_protected():
    return "JWT Auth: Access Granted"

# Route protégée avec contrôle de rôle (accès uniquement pour admin)
@app.route('/admin-only', methods=['GET'])
@jwt_required()
def admin_only():
    """Vérifie si l'utilisateur a un rôle 'admin'"""
    current_user = get_jwt_identity()
    user = users.get(current_user)

    if user and user['role'] == 'admin':
        return "Admin Access: Granted"

    return jsonify({"error": "Accès admin requis"}), 403

# Gestion des erreurs JWT
@jwt.unauthorized_loader
def handle_unauthorized_error(err):
    return jsonify({"error": "Token manquant ou invalide"}), 401

@jwt.invalid_token_loader
def handle_invalid_token_error(err):
    return jsonify({"error": "Token invalide"}), 401

@jwt.expired_token_loader
def handle_expired_token_error(err):
    return jsonify({"error": "Le token a expiré"}), 401

@jwt.revoked_token_loader
def handle_revoked_token_error(err):
    return jsonify({"error": "Le token a été révoqué"}), 401

@jwt.needs_fresh_token_loader
def handle_needs_fresh_token_error(err):
    return jsonify({"error": "Token frais requis"}), 401

# Démarrer l'application
if __name__ == '__main__':
    app.run(debug=True)

