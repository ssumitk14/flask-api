from flask import Flask
from flask_restful import Api, Resource

app = Flask(__name__)
api = Api(app)

class className(Resource):
    def get(self):
        return {"name":"sumit"}
    def post(self):
        return {"name":"Posted"}
api.add_resource(className,'/test')

if __name__ == "__main__":
    app.run(debug=True)

