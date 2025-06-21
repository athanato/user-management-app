from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
import os
import logging

app = Flask(__name__)

DB_HOST = os.getenv("DB_HOST", "localhost")
DB_USER = os.getenv("DB_USER", "user")
DB_PASS = os.getenv("DB_PASS", "pass")
DB_NAME = os.getenv("DB_NAME", "usersdb")

app.config["SQLALCHEMY_DATABASE_URI"] = f"postgresql://{DB_USER}:{DB_PASS}@{DB_HOST}/{DB_NAME}"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)

    def serialize(self):
        return {"id": self.id, "name": self.name}

@app.route("/users")
def get_users():
    try:
        users = User.query.all()
        return jsonify([u.serialize() for u in users])
    except Exception as e:
        app.logger.error(f"Error fetching users: {e}")
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG)
    with app.app_context():
        db.create_all()
    app.run(host="0.0.0.0", port=5000)
