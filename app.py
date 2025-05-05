from flask import Flask, jsonify, request
from pymongo import MongoClient
import os

app = Flask(__name__)

# MongoDB connection
client = MongoClient('mongodb://mongo:27017/')
db = client.flask_db
todos = db.todos

@app.route('/')
def index():
    return 'Flask with MongoDB Docker application!'

@app.route('/todos', methods=['GET'])
def get_todos():
    results = []
    for todo in todos.find():
        results.append({'id': str(todo['_id']), 'task': todo['task']})
    return jsonify(results)

@app.route('/todos', methods=['POST'])
def add_todo():
    task = request.json.get('task', '')
    if task:
        todo_id = todos.insert_one({'task': task}).inserted_id
        return jsonify({'id': str(todo_id), 'task': task})
    return jsonify({'error': 'Invalid task'}), 400

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)