from flask import Flask
from flask_restful import Api, Resource, reqparse

app = Flask(__name__)
api = Api(app)

## Taking arguments from PUT requests
## If any argumentsis not found while sending the PUT requests then None will automatically be added

video_put_args = reqparse.RequestParser()
video_put_args.add_argument("name",type=str, help="Name of the video")
video_put_args.add_argument("views",type=int, help="Views of the video")
video_put_args.add_argument("likes",type=int, help="Likes on the video")


class Video(Resource):

    def get(self,video_id):
        return {}
    def put(self,video_id):
        args = video_put_args.parse_args()
        return {video_id:args}

api.add_resource(Video, '/Video/<int:video_id>')

if __name__ =="__main__":
    app.run(debug=True)
