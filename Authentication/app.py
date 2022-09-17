from flask import Flask, request
from flask_restful import Resource,Api 
from flask_jwt import JWT, jwt_required 

from security import authenticate, identity 

app = Flask(__name__)
app.secret_key = 'nikki'
api = Api(app)

jwt = JWT(app, authenticate, identity) # created /auth

items = [] 

class Items(Resource):
    @jwt_required()
    def get(self,name):  
        item = next(filter(lambda x: x['name']==name,items), 'Item Not found') # next gives first item matched 
        # for item in items:
        #     if item['name'] == name:
        #         return item
        return {"item": item}, 200 if item else 404 
    
    def post(self,name):
        if next(filter(lambda x: x['name']==name,items), None) is not None:
            return {"message": "Item with name {} already exist".format(name)}, 400
        data = request.get_json()
        item = {"name": name,"price":data['price']}
        items.append(item)
        return item, 201 # code 201 is for created , 202 for accepted you can use when creating is taking long time

class ItemsList(Resource):
    def get(self):
        return {"item": items}

api.add_resource(Items,'/item/<string:name>')
api.add_resource(ItemsList, '/items')

app.run(port=5000, debug=True)