import requests
import json
import unittest


class TestFormsAPI(unittest.TestCase):
    def setUp(self):
        self.base_url = "http://127.0.0.1:8000"

    def test_post_contact_information(self):
        url = f"{self.base_url}/get_form/"
        data = {"mail": "android@mail.ru", "date": "2022-11-22", "tel": "+71112223344"}

        response = requests.post(url, data=json.dumps(data))
        self.assertEqual(response.status_code, 200)
        response_data = response.json()

        expected_response = "Contact Information"
        self.assertIn(expected_response, str(response_data.get('Response data', '')))

    def test_post_sms_form(self):
        url = f"{self.base_url}/get_form/"
        data = {"username": "user1", "phone number": "+7 111 222 11 22"}

        response = requests.post(url, data=json.dumps(data))
        self.assertEqual(response.status_code, 200)
        response_data = response.json()

        expected_response = "SMS Form"
        self.assertIn(expected_response, str(response_data.get('Response data', '')))

    def test_post_happy_birthday_form(self):
        url = f"{self.base_url}/get_form/"
        data = {"date of birth": "2022-11-11", "phone number": "+7 1231232233"}

        response = requests.post(url, data=json.dumps(data))
        self.assertEqual(response.status_code, 200)
        response_data = response.json()

        expected_response = "Happy Birthday Form"
        self.assertIn(expected_response, str(response_data.get('Response data', '')))

    def test_post_personal_details_form(self):
        url = f"{self.base_url}/get_form/"
        data = {"username": "user2", "birthday": "12.01.2002"}

        response = requests.post(url, data=json.dumps(data))
        self.assertEqual(response.status_code, 200)
        response_data = response.json()

        expected_response = "Personal Details"
        self.assertIn(expected_response, str(response_data.get('Response data', '')))

    def test_post_feedback_form(self):
        url = f"{self.base_url}/get_form/"
        data = {"username": "user3", "mail": "email@example.com"}

        response = requests.post(url, data=json.dumps(data))
        self.assertEqual(response.status_code, 200)
        response_data = response.json()

        expected_response = "Feedback Form"
        self.assertIn(expected_response, str(response_data.get('Response data', '')))

    def test_post_personal_information_form(self):
        url = f"{self.base_url}/get_form/"
        data = {"username": "user4", "birthday": "20.12.2010", "phone": "+77777777777", "email": "exampleof@email.ru"}

        response = requests.post(url, data=json.dumps(data))
        self.assertEqual(response.status_code, 200)
        response_data = response.json()

        expected_response = "Personal Information"
        self.assertIn(expected_response, str(response_data.get('Response data', '')))

    def test_post_invalid_form_1(self):
        url = f"{self.base_url}/get_form/"
        data = {"user": "user5", "msg": "message from user"}

        response = requests.post(url, data=json.dumps(data))
        self.assertEqual(response.status_code, 200)
        response_data = response.json()

        expected_response = "{'user': 'text', 'msg': 'text'}"
        self.assertIn(expected_response, str(response_data.get('Response data', '')))

    def test_post_invalid_form_2(self):
        url = f"{self.base_url}/get_form/"
        data = {"date of birth": "2022-11-11", "phone number": "+7 111 222 333 44"}

        response = requests.post(url, data=json.dumps(data))
        self.assertEqual(response.status_code, 200)
        response_data = response.json()

        expected_response = "{'date of birth': 'date', 'phone number': 'text'}"
        self.assertIn(expected_response, str(response_data.get('Response data', '')))

    def test_post_invalid_form_3(self):
        url = f"{self.base_url}/get_form/"
        data = {"date": "today", "mail": "mail@gmail.com", "tel": "+71112223344"}

        response = requests.post(url, data=json.dumps(data))
        self.assertEqual(response.status_code, 200)
        response_data = response.json()

        expected_response = "{'date': 'text', 'mail': 'email', 'tel': 'phone'}"
        self.assertIn(expected_response, str(response_data.get('Response data', '')))


if __name__ == '__main__':
    unittest.main()
