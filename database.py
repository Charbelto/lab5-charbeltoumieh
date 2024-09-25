from flask import Flask, request, jsonify  # added to top of file
from flask_cors import CORS  # added to top of file
from app import get_users, get_user_by_id, insert_user, update_user, delete_user

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})

@app.route('/api/users', methods=['GET'])
def api_get_users():
    return jsonify(get_users())

@app.route('/api/users/<user_id>', methods=['GET'])
def api_get_user(user_id):
    return jsonify(get_user_by_id(user_id))

@app.route('/api/users/add', methods=['POST'])
def api_add_user():
    user = request.get_json()
    return jsonify(insert_user(user))

@app.route('/api/users/update', methods=['PUT'])
def api_update_user():
    user = request.get_json()
    return jsonify(update_user(user))

@app.route('/api/users/delete/<user_id>', methods=['DELETE'])
def api_delete_user(user_id):
    return jsonify(delete_user(user_id))


@app.route('/api/users/patch/<user_id>', methods=['PATCH'])
def api_patch_user(user_id):
    user_data = request.get_json()
    existing_user = get_user_by_id(user_id)
    
    if not existing_user:
        return jsonify({"message": "User not found"}), 404

    # Update only fields that are provided in the request
    updated_user = {
        "name": user_data.get("name", existing_user["name"]),
        "email": user_data.get("email", existing_user["email"]),
        "phone": user_data.get("phone", existing_user["phone"]),
        "address": user_data.get("address", existing_user["address"]),
        "country": user_data.get("country", existing_user["country"]),
        "user_id": user_id
    }

    return jsonify(update_user(updated_user))


if __name__ == "__main__":
    # app.debug = True
    # app.run(debug=True)
    app.run()  # run app
