from flask import Flask
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)


class Welcome (Resource):

    def get(self):
        return 'Hello World!'


api.add_resource(Welcome, '/')

if __name__ == '__main__':
    app.run('0.0.0.0', '3333')
