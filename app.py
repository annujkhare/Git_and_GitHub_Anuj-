
from flask import Flask, jsonify, render_template

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/api")
def api():
    response = {
        "message": "JSON updated directly on main",
        "project": "Flask API",
        "status": "main-update"
    }

    return jsonify(response)


if __name__ == "__main__":
    app.run(debug=True)
