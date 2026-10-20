
from flask import Flask, jsonify, render_template, request
from pymongo import MongoClient
from datetime import datetime, timezone

app = Flask(__name__)

# Connect to MongoDB running on this computer.
mongo_client = MongoClient(
    "mongodb://localhost:27017/",
    serverSelectionTimeoutMS=3000
)

database = mongo_client["todos_db"]
todo_collection = database["todo_items"]


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/api")
def api():
    response = {
        "message": "JSON updated in the new branch",
        "project": "Git and GitHub DevOps Assignment",
        "status": "success",
        "branch": "AnuKhare_new",
        "version": 2
    }

    return jsonify(response)


@app.route("/submittodoitem", methods=["POST"])
def submit_todo_item():
    # Read the values submitted by the HTML form.
    item_name = request.form.get("itemName", "").strip()
    item_description = request.form.get(
        "itemDescription", ""
    ).strip()

    # Check that both fields contain information.
    if not item_name or not item_description:
        return "Both fields are required.", 400

    # Create a document to store in MongoDB.
    todo_item = {
        "itemName": item_name,
        "itemDescription": item_description,
        "createdAt": datetime.now(timezone.utc)
    }

    try:
        # Save the document in the database.
        result = todo_collection.insert_one(todo_item)

        return (
            f"To-Do item saved successfully! "
            f"Database ID: {result.inserted_id}<br>"
            f"<a href='/'>Add another item</a>"
        )

    except Exception:
        app.logger.exception("Could not save the To-Do item")
        return (
            "Could not save the item. Check your MongoDB service "
            "and connection.",
            500
        )


if __name__ == "__main__":
    app.run(debug=True)
