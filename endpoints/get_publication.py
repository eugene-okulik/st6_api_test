import requests
import allure
from endpoints.json_schemas import Publication
from endpoints.base_endpoint import BaseEndpoint


class GetPublication(BaseEndpoint):

    @allure.step('Get publication by its id')
    def get_by_id(self, post_id):
        self.response = requests.get(f'https://jsonplaceholder.typicode.com/posts/{post_id}')
        self.status_code = self.response.status_code
        self.response_json = self.response.json()

    @allure.step('Check that id is correct')
    def check_id_is_(self, post_id):
        assert self.response_json['id'] == post_id

    @allure.step('Check that schema is correct')
    def check_response_json_shema(self):
        Publication(**self.response_json)
