from extensions import db

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(150), nullable=False)
    content = db.Column(db.Text, nullable=False)
    user_id = db.Column(db.Integer, nullable=False)  # кто создал пост

    def to_dict(self):
        return {
            "id": self.id,
            "title": self.title,
            "content": self.content,
            "user_id": self.user_id
        }