from flask import Flask
from flask_restful import Api, Resource, reqparse, abort, fields, marshal_with
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow 
from flask import  request, jsonify
app = Flask(__name__)
api = Api(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
db = SQLAlchemy(app)
ma = Marshmallow(app)

class catalog(db.Model):
	item_id = db.Column(db.String, primary_key=True)
	number_in_stock = db.Column(db.Integer ,nullable=False)
	cost=  db.Column(db.Integer, nullable=False)
	topic = db.Column(db.String(100), nullable=False)
	titel=db.Column(db.String(100), nullable=False)

	def __repr__(self):
		return f"catalog2(number_in_stock = {number_in_stock}, cost = {cost}, topic = {topic},titel={titel})"



	

	
		

class ProductSchema(ma.Schema):
  class Meta:
    fields = ('item_id', 'number_in_stock', 'cost', 'topic','titel')

# Init schema
product_schema = ProductSchema()
products_schema = ProductSchema(many=True)
catalog_put_args = reqparse.RequestParser()
catalog_put_args.add_argument("number_in_stock", type=int, help="#stock not avalible", required=True)
catalog_put_args.add_argument("cost", type=int, help="cost not", required=True)
catalog_put_args.add_argument("topic", type=str, help="topic not", required=True)
catalog_put_args.add_argument("titel", type=str, help="topic not", required=True)
catalog_update_args = reqparse.RequestParser()
catalog_update_args.add_argument("number_in_stock", type=int, help="#stock not avalible")
catalog_update_args.add_argument("cost", type=int, help="cost not")
catalog_update_args.add_argument("topic", type=str, help="topic not")


catalog_update_args2 = reqparse.RequestParser()

catalog_update_args2.add_argument("item_id", type=str, help="#id")

catalog_update_args2.add_argument("topic", type=str, help="topic not")



catalog77_update_args = reqparse.RequestParser()

catalog77_update_args.add_argument("item_id", type=str, help="#id")


catalog88_update_args = reqparse.RequestParser()

catalog88_update_args.add_argument("cost", type=int, help="#id")
catalog88_update_args.add_argument("number_in_stock", type=int, help="#id")


resource_fields = {
	'item_id': fields.String,
	'number_in_stock': fields.Integer,
	'cost': fields.Integer,
	'topic': fields.String

	 
}


class catalog3(Resource):
	def patch(self ):
		args = catalog77_update_args.parse_args()
		result = catalog.query.filter_by(item_id=args['item_id']).first()
		if not result:
			return ({"exsist" :-1 }) 
		elif(result.number_in_stock)>0:
			x=result.number_in_stock
			result.number_in_stock = result.number_in_stock -1
			db.session.commit()
			return({"exsist" :x })

		    
		
		else:
		    return ({"exsist" :-2 })

		

api.add_resource(catalog3, "/book2")






if __name__ == "__main__":
	app.run(host="0.0.0.0", debug=True, port="7000" )