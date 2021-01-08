# from __main__ import db
from Intro import db
from datetime import datetime

class User(db.Model): # will have a table name of user (small u)
    id = db.Column(db.Integer,primary_key=True)
    username = db.Column(db.String(20),unique=True,nullable=False) # string of max 20 len
    email = db.Column(db.String(120), unique=True, nullable=False)
    image_file = db.Column(db.String(20),nullable=False,default='default.jpg')
    password = db.Column(db.String(60),nullable=False)
    posts = db.relationship('Post',backref='author',lazy='subquery') # backref is for... lazy (select,joined,dynamic,subquery)

    def __repr__(self):
        return f'User( {self.username}, {self.email}, {self.image_file})'

class Post(db.Model): # will have a table name of post (small p)
    id = db.Column(db.Integer,primary_key=True)
    title = db.Column(db.String(100),nullable=False)
    date_posted = db.Column(db.DateTime,nullable=False,default=datetime.utcnow)
    content = db.Column(db.Text,nullable=False)
    user_id = db.Column(db.Integer,db.ForeignKey('user.id'),nullable=False) #

    def __repr__(self):
        return f"Post( {self.title}, {self.date_posted} )"


# when we run directly from python, python calls the file "__main__"
# circular import : remember