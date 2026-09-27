from flask import Flask, jsonify

app = Flask(__name__)

users = [
    {
        "id": 1,
        "name": "Vishal"
    },
    {
        "id": 2,
        "name": "Rahul"
    }
]

@app.route("/")
def home():
    return "User Service is running Successfully"

@app.route("/users")
def get_users():
    return jsonify(users)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001)
