from flask import Flask, jsonify, request

app = Flask(__name__)

# In-memory storage for users
users = {
    "jane": {"username": "jane", "name": "Jane", "age": 28, "city": "Los Angeles"},
    "john": {"username": "john", "name": "John", "age": 30, "city": "New York"}
}

@app.route('/')
def home():
    return "Welcome to the Flask API!"

@app.route('/data')
def get_users():
    """Return a list of all usernames"""
    return jsonify(list(users.keys()))

@app.route('/status')
def status():
    """Return a status message"""
    return "OK"

@app.route('/users/<username>')
def get_user(username):
    """Return the full object for a given username"""
    user = users.get(username)
    if user:
        return jsonify(user)
    else:
        return jsonify({"error": "User not found"}), 404

@app.route('/add_user', methods=['POST'])
def add_user():
    """Add a new user to the users dictionary"""
    user_data = request.get_json()

    # Check if required fields are present
    if 'username' not in user_data:
        return jsonify({"error": "Username is required"}), 400

    username = user_data['username']

    # Check if the user already exists
    if username in users:
        return jsonify({"error": "User already exists"}), 400

    # Add the new user
    users[username] = user_data

    return jsonify({
        "message": "User added",
        "user": users[username]
    }), 201

if __name__ == "__main__":
    app.run(debug=True)

