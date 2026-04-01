from flask import Flask
from extensions import db, jwt, bcrypt
from routes import auth_bp

app = Flask(__name__)

# конфиг
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["JWT_SECRET_KEY"] = "super-secret-key"

# инициализация
db.init_app(app)
jwt.init_app(app)
bcrypt.init_app(app)

# роуты
app.register_blueprint(auth_bp, url_prefix="/auth")

# создать БД
with app.app_context():
    db.create_all()

if __name__ == "__main__":
    app.run(host="0.0.0.0",port=5000,debug=True)