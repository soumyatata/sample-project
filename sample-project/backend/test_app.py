import pytest
from app import app
import json

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client


# def test_submit_valid_data(client):
#     data={
#         'name':'Josh Don',
#         'email':'Josh.D@example.com'
#     }
#     response=client.post('/api/submit',json=data)
#     assert response.status_code==200
#     assert response.json['message']==f"Hello {data['name']}!"

def test_missing_name(client):
    data={
        'email':'Josh.D@example.com'
    }
    response=client.post('/api/submit',json=data)
    assert response.status_code==400
    assert response.json['error']=="Name is required"

def test_invalid_name_length(client):
    data={
        'name':'Jo','email':'Josh.D@example.com'
    }
    response=client.post('/api/submit',json=data)
    assert response.status_code==400
    assert response.json['error']=="Name length must be between 5 and 10 charcters"

def test_invalid_name_type(client):
    data={
        'name':123456,'email':'Josh.D@example.com'
    }
    response=client.post('/api/submit',json=data)
    assert response.status_code==400
    assert response.json['error']=="Name must be a string"
