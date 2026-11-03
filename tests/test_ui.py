import allure
import pytest
from selenium import webdriver
from pages.AniLibertyPage import AniLibertyPages


test_login = "*****"
test_pass = "*****"
ru_title_test = "Берсерк"
ro_title_test = "Kimetsu no Yaiba"


@pytest.fixture
def driver():
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")
    driver_instance = webdriver.Chrome(options=options)
    yield driver_instance
    driver_instance.quit()


@allure.epic("AniLiberty UI Тесты")
@allure.feature("Авторизация")
@allure.title("UI. Успешный вход в систему")
@allure.description("Позитивный тест: проверка авторизации "
                    "с валидными учетными данными через интерфейс.")
@allure.severity("blocker")
@allure.id("UI-2.0")
def test_ui_authorization(driver) -> None:
    page = AniLibertyPages(driver)
    page.open_home_page()
    page.login(test_login, test_pass)
    assert driver.current_url == "https://www.aniliberty.top/"


@allure.epic("AniLiberty UI Тесты")
@allure.feature("Поиск")
@allure.title("UI. Поиск релиза на русском языке")
@allure.description("Позитивный тест: проверка поискового запроса "
                    "по русскому названию аниме.")
@allure.severity("critical")
@allure.id("UI-2.1")
def test_ui_search_russian(driver) -> None:
    page = AniLibertyPages(driver)
    page.open_home_page()
    page.login(test_login, test_pass)
    page.open_search_modal()
    page.search_title(ru_title_test)
    page.open_first_search_result_by_href()

    assert page.is_watch_button_displayed()


@allure.epic("AniLiberty UI Тесты")
@allure.feature("Поиск")
@allure.title("UI. Поиск релиза на ромадзи")
@allure.description("Позитивный тест: проверка поискового запроса "
                    "по оригинальному названию (ромадзи).")
@allure.severity("critical")
@allure.id("UI-2.2")
def test_ui_search_romaji(driver) -> None:
    page = AniLibertyPages(driver)
    page.open_home_page()
    page.login(test_login, test_pass)
    page.open_search_modal()
    page.search_title(ro_title_test)
    page.open_first_search_result_by_href()

    assert page.is_watch_button_displayed()


@allure.epic("AniLiberty UI Тесты")
@allure.feature("Избранное")
@allure.title("UI. Добавление релиза в избранное")
@allure.severity("critical")
@allure.id("UI-2.3")
def test_ui_add_to_favorites(driver) -> None:
    page = AniLibertyPages(driver)
    page.open_home_page()
    page.login(test_login, test_pass)

    assert page.click_and_check_star_in_catalog()


@allure.epic("AniLiberty UI Тесты")
@allure.feature("Авторизация")
@allure.title("UI. Выход из аккаунта")
@allure.description("Позитивный тест: "
                    "проверка завершения пользовательской сессии "
                    "через меню профиля.")
@allure.severity("normal")
@allure.id("UI-2.4")
def test_ui_logout(driver) -> None:
    page = AniLibertyPages(driver)
    page.open_home_page()
    page.login(test_login, test_pass)
    page.logout()
    assert "auth" in driver.current_url or "login" in driver.current_url
