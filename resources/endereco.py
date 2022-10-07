from flask_restful import Resource, reqparse, current_app, marshal, marshal_with
from sqlalchemy import exc

from helpers.database import db

from model.endereco import Endereco
from model.error import Error, error_campos


parser = reqparse.RequestParser()
parser.add_argument('logradouro', required=True)


class Endereco(Resource):
    def get(self):
        current_app.logger.info("Get - Endereços")
        endereco = Endereco.query\
            .all()
        return endereco, 200

    def post(self):
        current_app.logger.info("Post - Endereços")
        try:
            # JSON
            args = parser.parse_args()
            logradouro = args['logradouro']

            # Endereco
            endereco = Endereco(logradouro)
            # Criação do Endereco.
            db.session.add(endereco)
            db.session.commit()
        except exc.SQLAlchemyError as err:
            current_app.logger.error(err)
            erro = Error(1, "Erro ao adicionar no banco de dados, consulte o adminstrador",
                         err.__cause__())
            return marshal(erro, error_campos), 500

        return 204

    def put(self, endereco_id):
        current_app.logger.info("Put - Endereço")
        try:
            # Parser JSON
            args = parser.parse_args()
            current_app.logger.info("Endereço: %s:" % args)
            # Evento
            logradouro = args['logradouro']

            Endereco.query \
                .filter_by(id=endereco_id) \
                .update(dict(logradouro=logradouro))
            db.session.commit()

        except exc.SQLAlchemyError:
            current_app.logger.error("Exceção")

        return 204

    def delete(self, endereco_id):
        current_app.logger.info("Delete - Endereço: %s:" % endereco_id)
        try:
            Endereco.query.filter_by(id=endereco_id).delete()
            db.session.commit()

        except exc.SQLAlchemyError:
            current_app.logger.error("Exceção")
            return 404

        return 204
