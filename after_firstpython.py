from flask import Flask
from flask_restful import Api, Resource, reqparse, abort, fields, marshal_with
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow 
from flask import  request, jsonify
import json
import datetime
import requests
app = Flask(__name__)
api = Api(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database1.db'
db = SQLAlchemy(app)
ma = Marshmallow(app)

class order(db.Model):
	order_id = db.Column(db.Integer, primary_key=True)
	book_id = db.Column(db.String(100) ,nullable=False)
	date=  db.Column(db.String(100), nullable=False)
	

	def __repr__(self):
		return f"order(book_id = {book_id}, date = {date})"
db.create_all()
class ProductSchema(ma.Schema):
  class Meta:
    fields = ('order_id', 'book_id', 'date')

# Init schema
product_schema = ProductSchema()
products_schema = ProductSchema(many=True)
catalog_put_args = reqparse.RequestParser()
catalog_put_args.add_argument("book_id", type=str, help="#stock not avalible", required=True)
catalog_put_args.add_argument("date", type=str, help="cost not", required=True)


catalog_update_args = reqparse.RequestParser()
catalog_update_args.add_argument("book_id", type=str, help="#stock not avalible")
catalog_update_args.add_argument("date", type=str, help="cost not")



catalog_update_args2 = reqparse.RequestParser()

catalog_update_args2.add_argument("order_id", type=int, help="#id")

catalog_update_args2.add_argument("date", type=str, help="topic not")

catalog_update_args3 = reqparse.RequestParser()



catalog_update_args3.add_argument("book_id", type=str, help="topic not")

catalog_update_args3.add_argument("date", type=str, help="topic not")
resource_fields = {
	'order_id': fields.Integer,
	'book_id': fields.String,
	'date': fields.String
	

	 
}

class order2(Resource):
	@marshal_with(resource_fields)
	def patch(self, order_id):
		args = catalog_update_args.parse_args()
		result = order.query.filter_by(order_id=order_id).first()
		if not result:
			abort(404, message="order doesn't exist, cannot update")

		if args['book_id']:
			result.book_id = args['book_id']
		if args['date']:
			result.date = args['date']
		
		db.session.commit()

		return result
api.add_resource(order2, "/edit_order/<int:order_id>")
class order3(Resource):
	@marshal_with(resource_fields)
	def put(self):
		catalog89_update_args = reqparse.RequestParser()
		catalog89_update_args.add_argument("item_id", type=str, help="#id")
		args = catalog89_update_args.parse_args()
		response = requests.patch("http://192.168.1.215:7000/" + "book2", {"item_id" : args['item_id'] })

   		
		temppp=json.loads( str(response.content, 'utf-8'))
		if(temppp['exsist']==-1):
		    abort(404, message="book  doesn't exist ")
		elif(temppp['exsist']==-2):
			abort(404, message="number in stoch is zero ")	
		else: 
		    video = order( book_id=args['item_id'], date=str(datetime.datetime.utcnow()))
		    
		    db.session.add(video)
		    db.session.commit()
		return video, 201  	
api.add_resource(order3, "/buy")




@app.route('/show_orders', methods=['GET'])
def get_products():
  all_products = order.query.all()
  result = products_schema.dump(all_products)
  return jsonify(result)
	


@app.route('/product/<id>', methods=['POST'])
def update_order(id):
  product = order.query.get(id)
  if not product:
	  return "order does not exsist"

  book_id = request.json['book_id']
  date = request.json['date']
  if (book_id):
	  product.book_id = book_id
  if(date):
	  product.date = date
  db.session.commit() 	  


  
  
  

  

  return product_schema.jsonify(product)





'''@app.route('/productdecraese/<id>', methods=['POST'])
def update_product5(id):
  product = order.query.get(id)

  
  

  product.number_in_stock = product.number_in_stock -1
  

  db.session.commit()

  return product_schema.jsonify(product)

@app.route('/productinecraese/<id>', methods=['POST'])
def update_product6(id):
  product = catalog.query.get(id)

  
  

  product.number_in_stock = product.number_in_stock + 1
  

  db.session.commit()

  return product_schema.jsonify(product)  





@app.route('/product/<id>', methods=['DELETE'])
def delete_product(id):
  product = catalog.query.get(id)
  db.session.delete(product)
  db.session.commit()

  return product_schema.jsonify(product)'''
if __name__ == "__main__":
	app.run(host="0.0.0.0", debug=True )