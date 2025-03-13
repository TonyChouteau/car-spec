from flask import Flask

from api import api
from app import app

server = Flask(__name__)

server.register_blueprint(api, url_prefix='/api')
server.register_blueprint(app, url_prefix='/')

if __name__ == "__main__":
    server.run(debug=True)
