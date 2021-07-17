from flask import Flask
from flask_restful import Api, Resource

app = Flask(__name__)
api = Api(app)

names = {"sumit":{"age":23, "gender":"male"},
        "amit":{"age":26,"gender":"male"}}

class className(Resource):
    def get(self,name):
        return names[name]

api.add_resource(className,"/test/<string:name>")

if __name__ == "__main__":
    app.run(debug=True)

