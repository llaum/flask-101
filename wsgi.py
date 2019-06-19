from flask import Flask, jsonify, abort
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
