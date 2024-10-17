from flask import Flask, render_template, request, jsonify
from pymongo import MongoClient

app = Flask(__name__)

# MongoDB connection
client = MongoClient('mongodb+srv://Aravind:Aravind%402041@cluster0.ykz5b.mongodb.net/')
db = client['python']
collection = db['user_info']

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit_details', methods=['POST'])
def submit_details():
    data = request.get_json()
    
    name = data.get('name')
    age = data.get('age')
    gender = data.get('gender')

    user_data = {
        'name': name,
        'age': age,
        'gender': gender
    }

    collection.insert_one(user_data)
    
    return jsonify({'message': 'hey nice '})

if __name__ == '__main__':
    app.run(debug=True)
