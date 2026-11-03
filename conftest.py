import pytest
import requests


base_url_api = "https://anilibria.top/api/v1"


@pytest.fixture(scope="session")
def auth_token():
    """Фикстура для авторизации и получения токена (выполняется один раз на сессию тестов)"""
    login_payload = {
        "login": "nasty_an@list.ru",
        "password": "Nasta2005"
    }
    
    response = requests.post(f"{base_url_api}/accounts/users/auth/login", json=login_payload)
    assert response.status_code == 200, f"Ошибка авторизации в фикстуре: {response.text}"
    
    data = response.json()
    token = data.get("token")
    assert token is not None, "Токен не найден в ответе сервера!"
    
    return token

@pytest.fixture
def auth_headers(auth_token):
    """Фикстура, которая возвращает готовые заголовки с Bearer-токеном для запросов"""
    return {
        "Authorization": f"Bearer {auth_token}"
    }
