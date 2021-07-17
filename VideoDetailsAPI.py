from flask import Flask
from flask_restful import Api, Resource, reqparse, abort, fields, marshal_with
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
api = Api(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
db = SQLAlchemy(app)


## Making svhema for database
class VideoModel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    views = db.Column(db.Integer, nullable=False)
    likes = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return f"Video(Name = {self.name}, views = {self.views}, Likes = {self.likes}"


# This should only be run once. Once the database is created, then either remove/comment db.create_all() line
#db.create_all()  # This will create the database model

# Taking arguments from PUT requests
# If any arguments is not found while sending the PUT requests then None will automatically be added

# To make the argument compulsary, just add the parameter required=True inside add_argument
video_put_args = reqparse.RequestParser()
video_put_args.add_argument("name", type=str, help="Name of the video", required=True)
video_put_args.add_argument("views", type=int, help="Views of the video", required=True)
video_put_args.add_argument("likes", type=int, help="Likes on the video", required=True)

resource_fields = {
    'id': fields.Integer,
    'name': fields.String,
    'views': fields.String,
    'likes': fields.String
}

class Video(Resource):
    @marshal_with(resource_fields)  # Used for serializing the instance of VideoModel class
    def get(self, video_id):
        result = VideoModel.query.filter_by(id=video_id).first()
        # result is just an instance of VideoModel class. We need to make this instance serializable so that we can
        # convert to json when we use the GET method.
        if not result:
            abort(404, message="Video not found...")
        return result

    @marshal_with(resource_fields)
    def put(self, video_id):
        args = video_put_args.parse_args()
        result = VideoModel.query.filter_by(id=video_id).first()
        if result:
            abort(409, message="Video ID already exist... Use new Video ID")

        video = VideoModel(id=video_id,name=args['name'],views=args['views'],likes=args['likes'])
        db.session.add(video)
        db.session.commit()
        return video
    '''
    def delete(self, video_id):
       
        del videos[video_id]
        return 'Video Deleted', 204
    '''

api.add_resource(Video, '/Video/<int:video_id>')

if __name__ == "__main__":
    app.run(debug=True)
