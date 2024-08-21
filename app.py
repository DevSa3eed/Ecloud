from flask import Flask, request, jsonify

app = Flask(__name__)

# In-memory data storage
users = {}

# Helper function to generate user ID
def generate_user_id():
    return str(len(users) + 1)

# Create a new user
@app.route('/users', methods=['POST'])
def create_user():
    user_data = request.json
    user_id = generate_user_id()
    users[user_id] = {
        'username': user_data['username'],
        'password': user_data['password'],
        'active': user_data['active']
    }
    return jsonify({'id': user_id, 'user': users[user_id]}), 201

# Read user details
@app.route('/users/<user_id>', methods=['GET'])
def get_user(user_id):
    user = users.get(user_id)
    if user:
        return jsonify({'id': user_id, 'user': user}), 200
    return jsonify({'error': 'User not found'}), 404

# Update user details
@app.route('/users/<user_id>', methods=['PUT'])
def update_user(user_id):
    user = users.get(user_id)
    if user:
        user_data = request.json
        users[user_id] = {
            'username': user_data.get('username', user['username']),
            'password': user_data.get('password', user['password']),
            'active': user_data.get('active', user['active'])
        }
        return jsonify({'id': user_id, 'user': users[user_id]}), 200
    return jsonify({'error': 'User not found'}), 404

# Delete a user
@app.route('/users/<user_id>', methods=['DELETE'])
def delete_user(user_id):
    if user_id in users:
        del users[user_id]
        return jsonify({'message': 'User deleted successfully'}), 200
    return jsonify({'error': 'User not found'}), 404

if __name__ == '__main__':
    app.run(debug=True)