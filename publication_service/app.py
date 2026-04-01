from flask import Flask, request, jsonify
from extensions import db
from models import Post

app = Flask(__name__)

# база (можешь потом заменить на PostgreSQL)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///posts.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db.init_app(app)

with app.app_context():
    db.create_all()

@app.route("/posts", methods=["POST"])
def create_post():
    data = request.json

    post = Post(
        title=data["title"],
        content=data["content"],
        user_id=data["user_id"]
    )

    db.session.add(post)
    db.session.commit()

    return jsonify(post.to_dict()), 201

@app.route("/posts", methods=["GET"])
def get_posts():
    posts = Post.query.all()
    return jsonify([p.to_dict() for p in posts])

@app.route("/posts/<int:post_id>", methods=["GET"])
def get_post(post_id):
    post = Post.query.get_or_404(post_id)
    return jsonify(post.to_dict())

if __name__ == "__main__":
    app.run(host="0.0.0.0",port=5002, debug=True)