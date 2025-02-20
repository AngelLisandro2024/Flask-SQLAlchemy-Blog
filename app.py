from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///blog.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)

class Post(db.Model):
    __tablename__ = "post"
    id = db.Column(db.Integer, primary_key=True)
    Titulo = db.Column(db.String, nullable=False)
    Fecha = db.Column(db.DateTime, default=datetime.now)
    Texto = db.Column(db.String, nullable=False)

@app.route("/")
def inicio():
    post = post.query.order_by(Post.fecha.desc()).all()
    return render_template("inicio.html", posts=post)

@app.route("/agregar")
def agregar():
    return render_template("agregar.html")


if __name__ == "__main__":
    app.run(debug=True)
