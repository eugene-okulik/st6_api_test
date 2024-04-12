import pytest
import requests
from pydantic import BaseModel
import allure
from endpoints.create_publication import CreatePublication
from endpoints.delete_publication import DeletePublication
from endpoints.get_publication import GetPublication


class Publication(BaseModel):
    userId: int
    id: int
    title: str
    body: str


payload = {
    "title": 12341,
    "Body": {},
    "userId": 'sdjfhsd'
}


@allure.feature('Publications')
@allure.story('Create publication')
@allure.title('Проверка того-то')
@pytest.mark.smoke
@pytest.mark.parametrize('title', ['My title', 45, [2, 5]], ids=['string', 'int', 'array'])
def test_create_publication_string(title, create_publication):
    payload = {
        "title": title,
        "Body": "My publication content",
        "userId": 1
    }
    create_publication.create_new_publication(payload=payload)
    create_publication.check_response_is_201()
    create_publication.check_title_is_(payload['title'])


def test_create_publication_without(create_publication):
    create_publication.create_new_publication_without_(['title', 'userId'])
    create_publication.check_response_is_201()
    create_publication.check_title_is_(payload['title'])


@allure.feature('Publications')
@allure.story('Get publication')
@pytest.mark.new_feature
def test_get_by_id(post_id, get_publication):
    post_id = 42
    get_publication.get_by_id(post_id)
    get_publication.check_response_is_200()
    get_publication.check_id_is_(post_id)
    get_publication.check_response_json_shema()


def test_delete_pub(post_id, delete_publication, get_publication):
    delete_publication.delete(post_id)
    delete_publication.check_response_is_200()
    get_publication.get_by_id(post_id)
    get_publication.check_response_is_404()
