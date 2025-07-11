import requests


BASE_URL = "http://localhost:8000"


def test_create_user_1():
    user_data = {"id": 1, "name": "John Doe1", "email": "john.doe1@example.com"}
    response = requests.post(
        f"{BASE_URL}/users",
        json=user_data,
    )
    assert response.status_code == 200
    assert response.json() == {
        "message": f"User {user_data['name']} created successfully"
    }


def test_create_user_2():
    user_data = {"id": 2, "name": "John Doe2", "email": "john.doe2@example.com"}
    response = requests.post(
        f"{BASE_URL}/users",
        json=user_data,
    )
    assert response.status_code == 200
    assert response.json() == {
        "message": f"User {user_data['name']} created successfully"
    }


def test_get_user():
    # First create a user to ensure it exists
    user_data = {"id": 3, "name": "Test User", "email": "test@example.com"}
    create_response = requests.post(f"{BASE_URL}/users", json=user_data)
    assert create_response.status_code == 200

    # Then get the user
    response = requests.get(f"{BASE_URL}/users/3")
    assert response.status_code == 200
    assert response.json() == user_data


def test_delete_user():
    # First create a user to ensure it exists
    user_data = {"id": 4, "name": "Delete Me", "email": "delete@example.com"}
    create_response = requests.post(f"{BASE_URL}/users", json=user_data)
    assert create_response.status_code == 200

    # Then delete the user
    response = requests.delete(f"{BASE_URL}/users/4")
    assert response.status_code == 200
    assert response.json() == {"message": "User deleted successfully"}
