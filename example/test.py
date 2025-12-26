import requests

def test_retrieve_api():
    url = "http://localhost:8080/retrieve"
    headers = {
        "Content-Type": "application/json",
        "Token": "ordinary_token"
    }
    payload = {
        "text": "什么是敏捷开发?"
    }

    response = requests.post(url, json=payload, headers=headers)
    print("Retrieve API Response:", response.json())


def test_clear_api():
    url = "http://localhost:8080/admin/clear"
    headers ={
        "Content-Type": "application/json",
        "Token": "ordinary_token"
    }

    response = requests.delete(url, headers=headers)
    print("Clear API Response with ordinary token:", response.json())

    headers = {
        "Content-Type": "application/json",
        "Token": "admin_token"
    }

    response = requests.delete(url, headers=headers)
    print("Clear API Response with admin token:", response.json())


if __name__ == "__main__":
    test_retrieve_api()
    test_clear_api()