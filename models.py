from datetime import datetime
from app import db

#add column borrowed, which shows: book is borrowed or staying on the shelf
class Homelibrary(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), index=True, unique=True)
    borrowed = db.Column(db.Boolean, default=False)  

    def __str__(self):
        return self.title
    
#class shows that one author can has a lot of books
class Author(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    author_name = db.Column(db.String(100), index=True)
    books = db.relationship('Homelibrary', backref=db.backref('author', lazy=True))

    def __str__(self):
        return self.author_name
    
  