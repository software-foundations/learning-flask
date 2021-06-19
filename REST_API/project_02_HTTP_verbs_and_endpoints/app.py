from flask import Flask, jsonify, request # use jsonify to cast list to json

app = Flask(__name__)

stores = [

	{
		'name': 'My store name',
		'items': [
			{
				'name': 'My item',
				'price': 15.99
			}
		]
	}
]

# POST -> used to receive data
# GET -> used to send data back only

# POST /store data: {name:}
@app.route('/store', methods=['POST'])
def create_store():
	request_data = request.get_json()
	new_store = {
		'name': request_data['name'],
		'items': []
	}

	stores.append(new_store)

	return new_store

# GET /store/<string:name>
# 'http://127.0.0.1:5000/store/some_name'
@app.route('/store/<string:name>', methods=['GET'])
def get_store(name):
	for store in stores:		
		if store['name'] == name:			
			return store
	return {'message': 'store not found'}

# GET /store
@app.route('/store', methods=['GET'])
def get_stores():
	return jsonify(stores), 200

# POST /store/<string:name>/item {name:, price:}
@app.route('/store/<string:name>/item', methods=['POST'])
def create_item_ins_store(name):
	request_data = request.get_json()
	for store in stores:
		if store['name'] == name:
			new_item = {
				'name': request_data['name'],
				'price': request_data['price']
			}
			store['items'].append(new_item)
			return new_item
	return {'message': 'store not found'}

# GET /store/<string:name>/item
@app.route('/store/<string:name>/item', methods=['GET'])
def get_items_in_store(name):
	for store in stores:
		if store['name'] == name:
			return jsonify(store['items'])
	return {'message': 'store not found'}				


app.run(port=5000)