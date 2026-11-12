import pytest
import requests

BASE_URL = "https://jsonplaceholder.typicode.com"

# 1. GET Request: Verify fetching a list of users
def test_get_users():
    response = requests.get(f"{BASE_URL}/users")
    assert response.status_code == 200, "Expected status code 200"
    
    data = response.json()
    assert isinstance(data, list), "Response should be a list"
    assert len(data) > 0, "User list should not be empty"
    assert "email" in data[0], "User object should contain an email field"

# 2. POST Request: Verify creating a new user resource
def test_create_user():
    payload = {
        "name": "Moumita Shee",
        "username": "moumita_qa",
        "email": "moumita@example.com"
    }
    response = requests.post(f"{BASE_URL}/users", json=payload)
    assert response.status_code == 201, "Expected status code 201 for resource creation"
    
    data = response.json()
    assert data["name"] == payload["name"]
    assert data["email"] == payload["email"]
    assert "id" in data

# 3. PUT Request: Verify updating an existing user
def test_update_user():
    updated_payload = {
        "id": 1,
        "name": "Moumita Updated",
        "email": "updated@example.com"
    }
    response = requests.put(f"{BASE_URL}/users/1", json=updated_payload)
    assert response.status_code == 200, "Expected status code 200"
    
    data = response.json()
    assert data["name"] == "Moumita Updated"

# 4. DELETE Request: Verify deleting a user
def test_delete_user():
    response = requests.delete(f"{BASE_URL}/users/1")
    assert response.status_code == 200, "Expected status code 200"

# 5. Negative Test Case: Verify handling of non-existent resource (404)
def test_get_invalid_user():
    response = requests.get(f"{BASE_URL}/users/9999")
    assert response.status_code == 404, "Expected 404 Not Found for invalid ID"
