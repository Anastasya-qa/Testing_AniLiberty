import allure
import requests

base_url = "https://anilibria.top/api/v1"
title_name = "Берсерк"
title_id = 7439


@allure.epic("AniLiberty API Тесты")
@allure.feature("Авторизация")
@allure.title("API. Успешная авторизация пользователя")
@allure.description("Позитивный тест: "
                    "проверка входа в систему с валидными данными.")
@allure.severity("blocker")
@allure.id("API-1.0")
def test_api_valid_login():
    json_payload = {
        "login": "*****",
        "password": "*****"
    }

    with allure.step("Отправка POST запроса авторизации"):
        response = requests.post(f"{base_url}/accounts/users/auth/login",
                                 json=json_payload)

    with allure.step("Проверка успешности ответа (статус 200)"):
        assert response.status_code == 200
        data = response.json()
        assert data is not None


@allure.epic("AniLiberty API Тесты")
@allure.feature("Избранное")
@allure.title("API. Получение избранного пользователя")
@allure.description("Позитивный тест: проверка получения списка избранного "
                    "для авторизованного пользователя.")
@allure.severity("critical")
@allure.id("API-1.1")
def test_api_get_user_favorites(auth_headers):
    with allure.step("Запрос списка избранного с токеном авторизации"):
        response = requests.get(
            f"{base_url}/accounts/users/me/favorites/releases",
            headers=auth_headers)

    with allure.step("Проверка статус-кода и наличия результатов"):
        assert response.status_code == 200
        favorites = response.json()
        assert favorites is not None


@allure.epic("AniLiberty API Тесты")
@allure.feature("Каталог")
@allure.title("API. Получение каталога релизов")
@allure.description("Позитивный тест: проверка получения "
                    "общего каталога аниме.")
@allure.severity("normal")
@allure.id("API-1.2")
def test_api_get_catalog_releases():
    with allure.step("Выполнение запроса каталога релизов"):
        response = requests.get(f"{base_url}/anime/catalog/releases")

    with allure.step("Проверка статус-кода"):
        assert response.status_code == 200


@allure.epic("AniLiberty API Тесты")
@allure.feature("Поиск")
@allure.title("API. Поиск релиза через поисковый эндпоинт")
@allure.description("Позитивный тест: проверка поискового запроса "
                    "по названию аниме.")
@allure.severity("critical")
@allure.id("API-1.3")
def test_api_search_releases_positive():
    params = {"query": title_name}

    with allure.step("Выполнение поискового запроса к API"):
        response = requests.get(f"{base_url}/app/search/releases",
                                params=params)

    with allure.step("Проверка статус-кода и наличия результатов"):
        assert response.status_code == 200
        results = response.json()
        assert results is not None


@allure.epic("AniLiberty API Тесты")
@allure.feature("Релизы")
@allure.title("API. Получение аниме по валидному ID")
@allure.description("Позитивный тест: проверка получения информации "
                    "о конкретном релизе по ID.")
@allure.severity("normal")
@allure.id("API-1.4")
def test_api_get_anime_by_valid_id():
    release_id = title_id
    with allure.step("Запрос релиза по ID"):
        response = requests.get(f"{base_url}/anime/releases/{release_id}")

    with allure.step("Проверка статус-кода"):
        assert response.status_code == 200
