from flask import Flask, jsonify, abort, request
app = Flask(__name__)

PRODUCTS = [
    { 'id': 1, 'name': 'Skello' },
    { 'id': 2, 'name': 'Socialive.tv' },
    { 'id': 3, 'name': 'iPhone' },
    { 'id': 4, 'name': 'Le Wagon' }
]
products_dict = { product["id"]: product for product in PRODUCTS }

@app.route('/')
def hello():
    return "Hello World!!!!"

@app.route('/api/v1/products')
def list_products():
    return jsonify(list(products_dict.values()))

@app.route('/api/v1/products/<int:product_id>')
def get_product(product_id):
    if product_id in products_dict:
        return jsonify(products_dict[product_id])
    abort(404)

@app.route('/api/v1/products/<int:product_id>', methods=['DELETE'])
def delete_product(product_id):
    if product_id in products_dict:
        del products_dict[product_id]
        return "", 204
    abort(404)

@app.route('/api/v1/products', methods=['POST'])
def post_products():
    product_name = request.get_json()["name"]
    next_id = max(list(products_dict.keys())) + 1
    products_dict[next_id] = dict(id=next_id, name=product_name)
    return jsonify(products_dict[next_id]), 201

@app.route('/api/v1/products/<int:product_id>', methods=['PATCH'])
def patch_product(product_id):
    if product_id in products_dict:
        new_product_name = request.get_json()["name"]
        if new_product_name == "":
            abort(422)
        products_dict[product_id] = dict(id=product_id, name=new_product_name)
        return "", 204
    abort(404)
