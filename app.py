from flask import Flask, render_template, jsonify
import random
import string

app = Flask(__name__)

# Function to generate a random password
def generate_password(length=12):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

# Route to render HTML page
@app.route('/')
def home():
    return render_template('index.html')

# API route to generate a password
@app.route('/generate', methods=['GET'])
def generate():
    password = generate_password()
    return jsonify({"password": password})

if __name__ == '__main__':
    app.run(debug=True)
 