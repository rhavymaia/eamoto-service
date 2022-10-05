from helpers.database import db


class Prefeitura(db.Model):
    __tablename__ = "tb_prefeitura"

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)

    def __init__(self, email):
        self.email = email

    def __repr__(self):
        return '<Prefeitura %r>' % self.email
