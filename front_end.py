from flask import Flask
from flask_restful import Api, Resource, reqparse, abort, fields, marshal_with
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow 
from flask import  request, jsonify
import requests
import json
app = Flask(__name__)
api = Api(app)

ma = Marshmallow(app)




	
        
        



class front_end1(Resource):
    
    def get(self,book_topic):
        response = requests.get("http://192.168.1.215:6000/" + "search", {"topic" :book_topic})
        temppp=json.loads( str(response.content, 'utf-8'))
        return jsonify(temppp)
api.add_resource(front_end1, "/search/<book_topic>")


@app.route('/lookup/<item_id>', methods=['GET'])   
def get2(item_id):
    response = requests.get("http://192.168.1.215:6000/" + "lookup", {"item_id" :item_id})
    temppp=json.loads( str(response.content, 'utf-8'))

    return jsonify({"titel" :temppp['titel']  ,"item_id" :temppp['item_id']})


@app.route('/buy/<item_id>', methods=['PATCH'])   
def buy(item_id):
    response = requests.put("http://192.168.1.251:5000/" + "buy", {"item_id" :item_id})
    temppp=json.loads( str(response.content, 'utf-8'))
    return jsonify(temppp)

    
@app.route('/increment_quantity_in_stock/<item_id>', methods=['put'])   
def inc(item_id):
    response = requests.post("http://192.168.1.50:6000/" + "book_incraese_in_stock", {"item_id" :item_id})
    temppp=json.loads( str(response.content, 'utf-8'))
    return jsonify(temppp)


@app.route('/deccrement_quantity_in_stock/<item_id>', methods=['put'])   
def dec(item_id):
    response = requests.post("http://192.168.1.215:6000/" + "book_decraese_in_stock", {"item_id" :item_id})
    temppp=json.loads( str(response.content, 'utf-8'))
    return jsonify(temppp)
    

if __name__ == "__main__":
	app.run(host="0.0.0.0", debug=True, port="8000" ,ssl_context=('cert.pem', 'key.pem') )


