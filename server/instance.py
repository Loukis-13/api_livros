from flask import Flask, Blueprint
from flask_restplus import Api

class Server():
    def __init__(self):
        self.app = Flask(__name__)
        self.blueprint = Blueprint('api', __name__, url_prefix='/api')
        self.api = Api(self.blueprint, doc= '/docs', title='Sample flask SQLAlchemy')
        self.app.register_blueprint(self.blueprint)

        self.app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
        self.app.config['PROPAGATE_EXCEPTIONS'] = True
        self.app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

        self.book_ns = self.api.namespace(name='Books', description='book related operation', path='/')

    def run(self):
        self.app.run(
            port=5000,
            debug=True,
            host='0.0.0.0'
            )

server = Server()