from unittest import TestCase

from starlette.testclient import TestClient

from main import app

client = TestClient(app)


class DemoTest(TestCase):

    def test_cat_facts(self):
        response = client.get("/asyncio-demo")
        self.assertEqual(5, len(response.json()["facts"]))
