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

    def test_create_product_id(self):
        response = self.client.post("/api/v1/products", json={"name": "Workelo"})
        self.assertTrue(response.status_code == 201)
        product_id = response.get_json()["id"]
        response = self.client.get(f"/api/v1/products/{product_id}")
        self.assertTrue(response.status_code == 200)
        self.assertEqual(response.get_json()["name"], "Workelo")

    def test_update_product_id(self):
        response = self.client.patch("/api/v1/products/1", json={"name": "Skello2"})
        self.assertTrue(response.status_code == 204)
        response = self.client.get("/api/v1/products/1")
        self.assertEqual(response.get_json()["name"], "Skello2")

    def test_update_product_id_with_empty_name(self):
        response = self.client.patch("/api/v1/products/1", json={"name": ""})
        self.assertTrue(response.status_code == 422)
