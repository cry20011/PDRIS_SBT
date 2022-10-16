from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from marshmallow import fields, Schema


app = Flask(__name__)
CORS(app)
app.config.from_object("app.config.Config")
db = SQLAlchemy(app)


class User(db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128), nullable=False)

    def __init__(self, name):
        self.name = name

class UserSchema(Schema):
    id = fields.Int(dump_only=True, required=True)
    name = fields.Str(required=True)


@app.route('/')
def hello():
    db.drop_all()
    db.create_all()
    db.session.commit()

    db.session.add(User(name="vasya"))
    db.session.add(User(name="vitalik"))
    db.session.commit()

    users = db.session.query(User).all()
    user_schema = UserSchema(many=True)
    return jsonify({"Users": user_schema.dump(users)})