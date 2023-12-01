from ext import db, app

class Comment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    comment = db.Column(db.String(200), nullable=False)



if __name__ == "__main__":
    with app.app_context():
        db.create_all()