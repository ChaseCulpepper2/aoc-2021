from flask import Flask
from flask_restful import Resource, Api, reqparse
import werkzeug
from apispec import APISpec
from marshmallow import Schema, fields
from apispec.ext.marshmallow import MarshmallowPlugin
from flask_apispec.extension import FlaskApiSpec
from flask_apispec.views import MethodResource
from flask_apispec import marshal_with, doc, use_kwargs
from services.solution_service import get_solution;

app = Flask(__name__)  # Flask app instance initiated
api = Api(app)  # Flask restful wraps Flask app around it.
app.config.update({
    'APISPEC_SPEC': APISpec(
        title='ChaseCulpepper2 AoC Solutions API',
        version='v1',
        plugins=[MarshmallowPlugin()],
        openapi_version='2.0.0'
    ),
    'APISPEC_SWAGGER_URL': '/swagger/',  # URI to access API Doc JSON
    'APISPEC_SWAGGER_UI_URL': '/swagger-ui/'  # URI to access UI of API Doc
})
docs = FlaskApiSpec(app)

class SolutionsResponseSchema(Schema):
    part_one = fields.Int()
    part_two = fields.Int()

class SolutionsRequestSchema(Schema):
    input = fields.Raw(type='file')

#  Restful way of creating APIs through Flask Restful
class AdventOfCodeSolutionAPI(MethodResource, Resource):
    def __init__(self):
        self.parser = reqparse.RequestParser()
    
    @doc(description='Get the Advent of Code solution', tags=['Solutions'])
    @use_kwargs(SolutionsRequestSchema)
    @marshal_with(SolutionsResponseSchema)  # marshalling
    def post(self, day):
        self.parser.add_argument('input', type=werkzeug.datastructures.FileStorage, location='files')
        return get_solution(day)


api.add_resource(AdventOfCodeSolutionAPI, '/solution/<int:day>')
docs.register(AdventOfCodeSolutionAPI)

if __name__ == '__main__':
    app.run(debug=True)