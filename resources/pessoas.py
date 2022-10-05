from model.pessoa import PessoaModel
from dao.pessoa import PessoaDAO
from flask import jsonify
from flask_restful import Resource, reqparse


class PessoasResource(Resource):
    def get(self):
        return jsonify(PessoaDAO.get_pessoas())

    def post(self):
        inserted_pessoa = {}

        # Leitura do json da requisição.
        parser = reqparse.RequestParser()
        parser.add_argument('nome')
        parser.add_argument('nascimento')
        parser.add_argument('email')
        parser.add_argument('telefone')
        args = parser.parse_args()

        print("Requisição via POST.")
        pessoa = PessoaModel(args['nome'], args['nascimento'],
                             args['email'], args['telefone'])
        inserted_pessoa = PessoaDAO.insert_pessoa(pessoa)

        return (inserted_pessoa, 200)


class PessoaResource(Resource):
    def get(self, pessoa_id):
        return jsonify(PessoaDAO.get_pessoa_id(pessoa_id))
