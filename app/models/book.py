from app import db

class Book(db.Model):
    __tablename__ = "book"
    id=db.Column(db.Integer, primary_key=True, autoincrement=True)
    title=db.Column(db.String)
    description=db.Column(db.String)
    