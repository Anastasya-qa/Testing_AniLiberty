import allure
import pytest
from selenium import webdriver
from pages.AniLibertyPage import AniLibertyPages


test_login = "nasty_an@list.ru"
test_pass = "Nasta2005"


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
@allure.description("Позитивный тест: проверка авторизации с валидными учетными данными через интерфейс.")
@allure.severity("blocker")
@allure.id("UI-1.1")
def test_ui_authorization(driver) -> None:
    page = AniLibertyPages(driver)
    page.open_home_page()
    page.login(test_login, test_pass)
    assert driver.current_url == "https://www.aniliberty.top/"


@allure.epic("AniLiberty UI Тесты")
@allure.feature("Поиск")
@allure.title("UI. Поиск релиза на русском языке")
@allure.description("Позитивный тест: проверка поискового запроса по русскому названию аниме.")
@allure.severity("critical")
@allure.id("UI-1.2")
def test_ui_search_russian(driver) -> None:
    page = AniLibertyPages(driver)
    page.open_home_page()
    page.login(test_login, test_pass)
    page.search_title("Берсерк")
    page.select_first_search_result()
    assert "anime" in driver.current_url


@allure.epic("AniLiberty UI Тесты")
@allure.feature("Избранное")
@allure.title("UI. Добавление релиза в избранное")
@allure.description("Позитивный тест: проверка добавления аниме в закладки через клик по иконке звезды.")
@allure.severity("critical")
@allure.id("UI-1.3")
def test_ui_add_to_favorites(driver) -> None:
    page = AniLibertyPages(driver)
    page.open_home_page()
    page.login(test_login, test_pass)
    # Кликаем на первый релиз на главной и добавляем в избранное
    page.select_first_search_result()
    page.click_star_icon()
    page.go_to_favorites()
    assert "favorites" in driver.current_url


@allure.epic("AniLiberty UI Тесты")
@allure.feature("Поиск")
@allure.title("UI. Поиск релиза на ромадзи")
@allure.description("Позитивный тест: проверка поискового запроса по оригинальному названию (ромадзи).")
@allure.severity("critical")
@allure.id("UI-1.4")
def test_ui_search_romaji(driver) -> None:
    page = AniLibertyPages(driver)
    page.open_home_page()
    page.login(test_login, test_pass)
    page.search_title("Kimetsu no Yaiba")
    page.select_first_search_result()
    assert "anime" in driver.current_url


@allure.epic("AniLiberty UI Тесты")
@allure.feature("Авторизация")
@allure.title("UI. Выход из аккаунта (логаут)")
@allure.description("Позитивный тест: проверка завершения пользовательской сессии через меню профиля.")
@allure.severity("normal")
@allure.id("UI-1.5")
def test_ui_logout(driver) -> None:
    page = AniLibertyPages(driver)
    page.open_home_page()
    page.login(test_login, test_pass)
    page.logout()
    assert "auth" in driver.current_url or "login" in driver.current_url
