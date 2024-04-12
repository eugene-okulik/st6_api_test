import pytest
from endpoints.create_publication import CreatePublication
from endpoints.delete_publication import DeletePublication
from endpoints.get_publication import GetPublication


@pytest.fixture()
def post_id(create_publication):
    create_publication.create_new_publication()
    post_id = create_publication.response_json['id']
    yield post_id
    DeletePublication().delete(post_id)


@pytest.fixture()
def create_publication():
    return CreatePublication()


@pytest.fixture()
def get_publication():
    return GetPublication()


@pytest.fixture()
def delete_publication():
    return DeletePublication()
