import pytest


@pytest.fixture
def create_user(django_user_model):
    def make_user(**kwargs):
        return django_user_model.objects.create_user(
            username='root',
            password='12345678hola',
            email='root@gmail.com'
        )
    return make_user
