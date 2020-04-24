from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(255), nullable=False)
    password = db.Column(db.String(255), nullable=False)
    address = db.Column(db.String(255), nullable=False)

    def getDict(self):
        dict = {
            'id': self.id,
            'username': self.username,
            'password': self.password,
            'address': self.address
        }
        return dict
