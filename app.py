from flask import Flask
from flask_restful import Api
from flask_cors import CORS  # added to top of file
from resources.index import IndexResource
#from resources.pessoas import PessoasResource, PessoaResource

from helpers.database import db

# CORS
app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})

# SQLAlchemy
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////aemotor.db'
db.init_app(app)

api = Api(app)

api.add_resource(IndexResource, '/')
#api.add_resource(PessoasResource, '/pessoas')
#api.add_resource(PessoaResource, '/pessoas/<pessoa_id>')

if __name__ == '__main__':
    app.run(debug=False)
