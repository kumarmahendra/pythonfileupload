from flask import Flask
from flask_restful import Resource, Api, reqparse
import werkzeug, os

app = Flask(__name__)
api = Api(app)

UPLOAD_FOLDER = '/Users/Guest/Documents'

parser = reqparse.RequestParser()
parser.add_argument('file',type=werkzeug.datastructures.FileStorage, location='files')


class HelloWorld(Resource):
    def get(self):
        return {'hello': 'world'}


class fileUpload(Resource):
    decorators=[]

    def post(self):
        data = parser.parse_args()
        if data['file'] == "":
            return {
                    'data':'',
                    'message':'No file found',
                    'status':'error'
                    }
        file = data['file']

        if file:
            filename = file.filename
            file.save(os.path.join(UPLOAD_FOLDER,filename))
            return {
                    'data':'',
                    'message':'File uploaded',
                    'status':'success'
                    }
        return {
                'data':'',
                'message':'Something went wrong',
                'status':'error'
                }


api.add_resource(HelloWorld, '/')
api.add_resource(fileUpload,'/upload')

if __name__ == '__main__':
    app.run(debug=True)
