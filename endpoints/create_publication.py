import requests
import allure
from endpoints.base_endpoint import BaseEndpoint
import logging
logging.getLogger(__name__)

HEADERS = {
    'Content-type': 'application/json'
}
PAYLOAD = {
    "title": 'title',
    "Body": "My publication content",
    "userId": 1
}


class CreatePublication(BaseEndpoint):

    @allure.step('Send post request')
    def create_new_publication(self, payload=None, headers=None):
        headers = headers if headers else HEADERS
        logging.info(f'Headers for publication {headers}')
        logging.info(f'Payload for publication {payload}')
        self.response = requests.post('https://jsonplaceholder.typicode.com/posts', json=payload, headers=headers)
        self.status_code = self.response.status_code
        self.response_json = self.response.json()

    def create_new_publication_without_(self, parameters: list, headers=None):
        headers = headers if headers else HEADERS
        for param in parameters:
            del PAYLOAD[param]
        print(PAYLOAD)
        self.response = requests.post('https://jsonplaceholder.typicode.com/posts', json=PAYLOAD, headers=headers)
        self.status_code = self.response.status_code
        self.response_json = self.response.json()

    @allure.step('Check that status code is 201')
    def check_response_is_201(self):
        assert self.status_code == 201

    @allure.step('Check that title is correct')
    def check_title_is_(self, title):
        assert self.response_json['title'] == title
