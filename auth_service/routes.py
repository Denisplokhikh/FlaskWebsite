from flask import Blueprint, request, jsonify
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity

from extensions import db, bcrypt
from models import User

auth_bp = Blueprint("auth", __name__)

@auth_bp.route("/register", methods=["POST"])
def register():
    data = request.get_json()

    username = data.get("username")
    password = data.get("password")

    if User.query.filter_by(username=username).first():
        return jsonify({"msg": "User exists"}), 400

    hashed = bcrypt.generate_password_hash(password).decode("utf-8")

    user = User(username=username, password=hashed)
    db.session.add(user)
    db.session.commit()

    return jsonify({"msg": "Created"})


@auth_bp.route("/login", methods=["POST"])
def login():
    data = request.get_json()

    user = User.query.filter_by(username=data.get("username")).first()

    if not user or not bcrypt.check_password_hash(user.password, data.get("password")):
        return jsonify({"msg": "Bad credentials"}), 401

    token = create_access_token(identity=user.username)

    return jsonify({"access_token": token})


@auth_bp.route("/profile")
@jwt_required()
def profile():
    user = get_jwt_identity()
    return jsonify({"user": user})