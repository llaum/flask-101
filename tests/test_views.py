from flask_testing import TestCase
from wsgi import app

class TestViews(TestCase):
    def create_app(self):
        app.config['TESTING'] = True
        return app

    def test_products_json(self):
        response = self.client.get("/api/v1/products")
        products = response.json
        self.assertIsInstance(products, list)
        self.assertGreater(len(products), 2) # 2 is not a mistake here.

    def test_get_product_id_json(self):
        response = self.client.get("/api/v1/products/1")
        self.assertIsInstance(response.json, dict)
        self.assertTrue(response.status_code == 200)

    def test_get_product_id_not_found(self):
        response = self.client.get("/api/v1/products/1000000")
        self.assertTrue(response.status_code == 404)

    def test_delete_product_id(self):
        response = self.client.delete("/api/v1/products/3")
        self.assertTrue(response.status_code == 204)
        response = self.client.get("/api/v1/products/3")
        self.assertTrue(response.status_code == 404)

    def test_delete_product_id_not_found(self):
        response = self.client.delete("/api/v1/products/1000000")
        self.assertTrue(response.status_code == 404)
