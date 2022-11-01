from unittest import TestCase
from app import create_app
import json


class Test(TestCase):
    def test_sort_without_params(self):
        app = create_app()
        with app.test_client() as client:
            response = client.get('/')

            self.assertEqual(response.status_code, 400)
            self.assertEqual(response.text, 'Input params missing')

    def test_sort_without_sortkey(self):
        app = create_app()
        with app.test_client() as client:
            response = client.get('/?limit=10')

            self.assertEqual(response.status_code, 400)
            self.assertEqual(response.text, 'Input params missing')

    def test_sort_without_limit(self):
        app = create_app()
        with app.test_client() as client:
            response = client.get('/?sortKey=views')

            self.assertEqual(response.status_code, 400)
            self.assertEqual(response.text, 'Input params missing')

    def test_sort_with_invalid_sortkey(self):
        app = create_app()
        with app.test_client() as client:
            response = client.get('/?limit=5&sortKey=abc')

            self.assertEqual(response.status_code, 400)
            self.assertEqual(response.text, 'Invalid Sort Key')

    def test_sort_with_views(self):
        app = create_app()
        with app.test_client() as client:
            response = client.get('/?limit=5&sortKey=relevanceScore')

            self.assertEqual(response.status_code, 200)
            self.assertEqual(json.loads(response.get_data()), {"count":5,"data":[{"relevanceScore":0.1,"url":"www.example.com/abc1","views":1000},{"relevanceScore":0.1,"url":"www.wikipedia.com/abc1","views":11000},{"relevanceScore":0.2,"url":"www.example.com/abc2","views":2000},{"relevanceScore":0.2,"url":"www.wikipedia.com/abc2","views":12000},{"relevanceScore":0.3,"url":"www.example.com/abc3","views":3000}]})

    def test_sort_with_relevancescore(self):
        app = create_app()
        with app.test_client() as client:
            response = client.get('/?limit=5&sortKey=views')

            self.assertEqual(response.status_code, 200)
            self.assertEqual(json.loads(response.get_data()), {"count":5,"data":[{"relevanceScore":0.1,"url":"www.example.com/abc1","views":1000},{"relevanceScore":0.2,"url":"www.example.com/abc2","views":2000},{"relevanceScore":0.3,"url":"www.example.com/abc3","views":3000},{"relevanceScore":0.4,"url":"www.example.com/abc4","views":4000},{"relevanceScore":0.5,"url":"www.example.com/abc5","views":5000}]})


if __name__ == "__main__":
    test = Test()