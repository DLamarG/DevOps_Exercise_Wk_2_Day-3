
from flask import Flask, jsonify

# We create a Flask application by initializing the  object.
app = Flask(__name__)

@app.route('/')
def index():
    data = 'Hello world!'
    return jsonify(data)


# Create some sample student data
students = [
    {'id': '1', 'first_name': 'John', 'last_name': 'Doe', 'age': '18', 'grade': 'A'},
    {'id': '2', 'first_name': 'Jane', 'last_name': 'Smith', 'age': '19', 'grade': 'B'},
    {'id': '3', 'first_name': 'Bob', 'last_name': 'Johnson', 'age': '20', 'grade': 'C'},
]

# We define a route `/students` that responds to GET requests.
@app.route('/students', methods=['GET'])
def get_students():
    return jsonify(students)

# If name = main prevents a codeblock from being run as a module import.
# Basically, it will only run if you manually execute the script.
if __name__ == '__main__':
    app.run(debug=True, port=8000) # Flask tries to run on port 5000 by default but it's sometimes occupied by a different function. Let's tell flask to utilize port 8000 instead
