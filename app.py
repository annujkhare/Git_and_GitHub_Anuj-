
from flask import Flask, jsonify, render_template

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/api")
def api():
    response = {
        "message": "Updated JSON from AnujKhare_new branch",
        "name": "Git and GitHub DevOps Assignment",
        "status": "success",
        "version": 2
    }

    return jsonify(response)

if __name__ == "__main__":
    app.run(debug=True)
