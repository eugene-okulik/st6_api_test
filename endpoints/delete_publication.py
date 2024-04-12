import requests
import allure
from endpoints.base_endpoint import BaseEndpoint


class DeletePublication(BaseEndpoint):

    @allure.step('Delete publication')
    def delete(self, post_id):
        self.response = requests.delete(f'https://jsonplaceholder.typicode.com/posts/{post_id}')
        self.status_code = self.response.status_code
