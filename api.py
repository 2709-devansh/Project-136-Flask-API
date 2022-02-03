from flask import Flask, jsonify, request
from data import data

app = Flask(__name__)

@app.route('/')
def home():
    return jsonify({
        "data":data,
        "message":"succesful"
    }), 404

@app.route('/stars')
def stars():
    name = request.args.get("name")
    star_data = next(i for i in data if i["name"] == name)
    return jsonify({
        "data":star_data,
        "message":"succesful"
    }), 404

if __name__ == "__main__":
    app.run()