from flask import Flask
from flask_restful import Api
from flask_cors import CORS
from resources.index import IndexResource

from helpers.database import db, migrate

from resources.endereco import Endereco
from resources.pessoa import Pessoa

# CORS
app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})

# SQLAlchemy
# postgresql://username:password@localhost:5432/your_database
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://pweb:123456@localhost:5432/aemotor"

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)
migrate.init_app(app, db)

api = Api(app)

api.add_resource(IndexResource, '/')
api.add_resource(Endereco, '/enderecos')
api.add_resource(Pessoa, '/pessoas')
#api.add_resource(PessoaResource, '/pessoas/<pessoa_id>')

if __name__ == '__main__':
    app.run(debug=False)
