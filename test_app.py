import pytest
import json
from app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_health_check(client):
    response = client.get('/api/health')
    assert response.status_code == 200
    data = json.loads(response.data)
    assert data['status'] == 'ok'

def test_get_students(client):
    response = client.get('/api/patients')
    assert response.status_code == 200
    data = json.loads(response.data)
    assert 'name' in data
    assert 'condition' in data

def test_get_unkown(client):
    response = client.get('/api/patients/5')
    assert response.status_code == 200
    data = json.loads(response.data)
    assert '404' in data
    
def test_add_student_valid(client):

    response = client.get('/api/patients/add')
    assert response.status_code == 200
    data = json.loads(response.data)
    assert '404' in data


    

