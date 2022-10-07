from helpers.database import db


class Endereco(db.Model):
    __tablename__ = "tb_endereco"

    id = db.Column(db.Integer, primary_key=True)
    logradouro = db.Column(db.String(80), nullable=False)

    def __init__(self, logradouro):
        self.logradouro = logradouro

    def __repr__(self):
        return '<Address %r>' % self.logradouro
