import pytest
from rest_framework import status
from rest_framework.reverse import reverse_lazy

from apps.models import Category


@pytest.mark.django_db
class TestAdvert:
    def test_create_task(self,api_client) -> None:
        payload = {
            'name': 'Food'
        }
        url = reverse_lazy('category-list')
        response = api_client.post(url, payload)
        print(response)
        category = Category.objects.first()
        assert response.status_code == status.HTTP_201_CREATED
        assert category is not None
        assert category.name == payload['name']


    def test_pytest_working(self):
        assert True == True




