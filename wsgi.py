from flask import Flask, jsonify
app = Flask(__name__)

PRODUCTS = [
    { 'id': 1, 'name': 'Skello' },
    { 'id': 2, 'name': 'Socialive.tv' }
]

@app.route('/')
def hello():
    return "Hello World!!!!"

@app.route('/api/v1/products')
def list_products():
    return jsonify(PRODUCTS)
