from flask import Flask, request, jsonify, render_template, redirect, url_for
from flask_bcrypt import Bcrypt
from pymongo import MongoClient
from bson.objectid import ObjectId
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

app = Flask(__name__, static_folder='static')
bcrypt = Bcrypt(app)

# MongoDB Atlas connection
client = MongoClient(os.environ.get('MONGODB_URI'))
db = client['user_database']
users_collection = db['users']

@app.route('/')
def index():
    users = users_collection.find()
    return render_template('index.html', users=users)

# Create new user
@app.route('/users/add', methods=['POST'])
def create_user():
    name = request.form.get('name')
    email = request.form.get('email')
    password = request.form.get('password')
    hashed_password = bcrypt.generate_password_hash(password).decode('utf-8')
    
    user_id = users_collection.insert_one({
        'name': name,
        'email': email,
        'password': hashed_password
    }).inserted_id
    return redirect(url_for('index'))

# Edit user
@app.route('/users/edit/<id>', methods=['POST'])
def edit_user(id):
    user = users_collection.find_one({'_id': ObjectId(id)})
    password = request.form.get('password')
    
    if bcrypt.check_password_hash(user['password'], password):
        name = request.form.get('name')
        email = request.form.get('email')
        
        users_collection.update_one(
            {'_id': ObjectId(id)},
            {'$set': {
                'name': name,
                'email': email
            }}
        )
        return redirect(url_for('index'))
    return 'Invalid password', 401

# Delete user
@app.route('/users/delete/<id>', methods=['POST'])
def delete_user(id):
    user = users_collection.find_one({'_id': ObjectId(id)})
    if user:
        users_collection.delete_one({'_id': ObjectId(id)})
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
