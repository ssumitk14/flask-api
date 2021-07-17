from flask import Flask
from flask_restful import Api, Resource, reqparse,abort

app = Flask(__name__)
api = Api(app)

## Taking arguments from PUT requests
## If any argumentsis not found while sending the PUT requests then None will automatically be added

#To make the argument compulsary, just add the parameter required=True inside add_argument
video_put_args = reqparse.RequestParser()
video_put_args.add_argument("name",type=str, help="Name of the video",required=True)
video_put_args.add_argument("views",type=int, help="Views of the video",required=True)
video_put_args.add_argument("likes",type=int, help="Likes on the video",required=True)

##Storing the data

videos = {}

def abort_if_video_id_doesnt_exist(video_id):
    '''
    :param video_id:
    :return: Message if video_id not available.
    '''
    if video_id not in videos.keys():
        abort(404, message="Video not found...")

def abort_if_video_id_exist(video_id):
    '''
    :param video_id:
    :return: Message if video_id is available.
    '''
    if video_id in videos.keys():
        abort(404, message="Video already exist...")

class Video(Resource):
    def get(self,video_id):
        abort_if_video_id_doesnt_exist(video_id)
        return videos[video_id]
    def put(self,video_id):
        abort_if_video_id_exist(video_id)
        args = video_put_args.parse_args()
        videos[video_id] = args
        return videos[video_id], 201

    def delete(self,video_id):
        abort_if_video_id_doesnt_exist(video_id)
        del videos[video_id]
        return 'Video Deleted',204


api.add_resource(Video, '/Video/<int:video_id>')

if __name__ =="__main__":
    app.run(debug=True)
