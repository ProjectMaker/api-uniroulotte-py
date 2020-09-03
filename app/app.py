from flask import Flask
from flask_cors import CORS
from flask_restplus import Api
from mongoengine import connect
from werkzeug.contrib.fixers import ProxyFix
from flask_jwt_extended import JWTManager

from config import get_config
from controller.user_controller import ns as ns_user
from controller.session_controller import ns as ns_session
from controller.devis_controller import ns as ns_devis

app = Flask(__name__)
CORS(app,
     origins=["https://devis.uni-roulotte.fr"],
     supports_credentials=True,
     allow_headers=["Access-Control-Allow-Credentials", "Content-Type"]
     )
app.config.from_object(get_config())
app.wsgi_app = ProxyFix(app.wsgi_app)

app.url_map.strict_slashes = False

app.config['JWT_TOKEN_LOCATION'] = ['cookies']
app.config['JWT_COOKIE_SECURE'] = False
app.config['JWT_COOKIE_CSRF_PROTECT'] = False
jwt = JWTManager(app)

api = Api(app, version='3.0', title='Simulateur de devis')

api.add_namespace(ns_user, path='/api/user')
api.add_namespace(ns_session, path='/api/session')
api.add_namespace(ns_devis, path='/api/devis')

if __name__ == "__main__":
    connect('uniroulotte', host='mongodb://root:Rudeboy788@ds137605.mlab.com:37605/uniroulotte', retryWrites=False)
    app.run(host='0.0.0.0', debug=True)

