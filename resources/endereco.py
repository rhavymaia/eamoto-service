from model.endereco import Endereco
from flask import jsonify
from flask_restful import Resource, marshal_with, reqparse, current_app, marshal


class Endereco(Resource):
    def get(self):
        current_app.logger.info("Get - Endereços")
        endereco = Endereco.query\
            .order_by(Endereco.logradouro)\
            .all()
        return endereco, 200
