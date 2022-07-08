from http import HTTPStatus
from django.test import TestCase


class DynamicFormTest(TestCase):
    def test_get(self):
        response = self.client.get("/userform/")

        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertContains(response, "<h1>Input your data</h1>", html=True)

    def test_post_success(self):
        response = self.client.post("/userform/", data={"input_name0": "Something interesting from my life"})

        self.assertEqual(response.status_code, HTTPStatus.FOUND)
        self.assertEqual(response["Location"], "/done/")

    def test_post_success_more(self):
        response = self.client.post("/userform/", data={
            "input_name0": "Something interesting from my life",
            "input_name1": "Something interesting from my life",
            "input_name2": "Something interesting from my life",
            "input_name3": "Something interesting from my life",
        })

        self.assertEqual(response.status_code, HTTPStatus.FOUND)
        self.assertEqual(response["Location"], "/done/")

    def test_post_error(self):
        user_input = 'Something interesting from my life, but nothing, maybe'
        response = self.client.post("/userform/", data={"input_name0": user_input})

        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertEqual(len(user_input) <= 40, False)
