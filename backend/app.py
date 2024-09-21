from flask import Flask, request
from flask import render_template, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/login")
def login():
    return render_template("Login.html")
@app.route("/signup")
def signup():
    return render_template("Signup.html")
"""
@app.route("/signup", methods=['POST'])
def signup():
    data = request.get_json()

    Name = data.get('name')
    Email = data.get('email')
    Username = data.get('username')
    Passw = data.get('password')
    Phno = data.get('phonenumber')
    YOStudy = data.get('yostudy')

    print(Name)
    return render_template("Signup.html")

if __name__ == '__main__':
    app.run(debug = True)
"""