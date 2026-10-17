#Esse é o arquivo que inicia o programa e unifica tudo
from flask import Flask
from rotas.public_views import public_bp
app = Flask(__name__)
app.register_blueprint(public_bp)


if __name__ == '__main__':
    app.run(host='localhost', debug=True)