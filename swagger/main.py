from flask import Flask
from flask_restful import Resource,Api 
from swagger_ui import api_doc, flask_api_doc
# from flasgger import Swagger, LazyString, LazyJSONEncoder
# from flasgger import swag_from


app = Flask(__name__)
api = Api(app)

spec_string = '{"openapi":"3.0.1","info":{"title":"python-swagger-ui test api","description":"python-swagger-ui test api","version":"1.0.0"},"servers":[{"url":"http://127.0.0.1:8989/api"}],"tags":[{"name":"default","description":"default tag"}],"paths":{"/hello/world":{"get":{"tags":["default"],"summary":"output hello world.","responses":{"200":{"description":"OK","content":{"application/text":{"schema":{"type":"object","example":"Hello World!!!"}}}}}}}},"components":{}}'
api_doc(app, config_spec=spec_string, url_prefix='/api/doc', title='API doc')


# @swag_from("hello_world.yml", methods=['GET'])
@app.route("/student",methods=['GET'])
def get(self):
    return {"student": "Nikki"}

@app.route("/hello")
def hello_world():
    return "Hello World!!!"



# api.add_resource(Student,'/student/<string:name>')

app.run(port=5000)