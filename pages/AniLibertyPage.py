import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class AniLibertyPages:
    """Класс страниц для проекта AniLiberty (Page Object Model)"""

    def __init__(self, driver: WebDriver) -> None:
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    @allure.step("Открыть главную страницу авторизации AniLiberty")
    def open_home_page(self) -> None:
        self.driver.get("https://www.aniliberty.top/app/auth/login")

    @allure.step("Выполнить авторизацию с логином: {login}")
    def login(self, login: str, password: str) -> None:
        login_input = self.wait.until(
            EC.presence_of_element_located((By.NAME, "login"))
        )
        login_input.clear()
        login_input.send_keys(login)

        password_input = self.wait.until(
            EC.presence_of_element_located((By.NAME, "current-password"))
        )
        password_input.clear()
        password_input.send_keys(password)

        submit_btn = self.wait.until(
            EC.element_to_be_clickable(
                (By.CSS_SELECTOR, "button.v-btn, button[type='button']")
            )
        )
        submit_btn.click()

        self.wait.until(lambda driver: "auth/login" not in driver.current_url)

    @allure.step("Ввести поисковый запрос: {query}")
    def search_title(self, query: str) -> None:
        input_field = self.wait.until(
            EC.presence_of_element_located(
                (By.CSS_SELECTOR, "input[placeholder*='Введите название аниме']")
            )
        )
        input_field.clear()
        input_field.send_keys(query)

    @allure.step("Выбрать первый результат из списка поиска")
    def select_first_search_result(self) -> None:
        first_item = self.wait.until(
            EC.element_to_be_clickable(
                (By.CSS_SELECTOR, ".v-list-item, .v-card")
            )
        )
        first_item.click()

    @allure.step("Добавить аниме в избранное (клик по кнопке со звездой)")
    def click_star_icon(self) -> None:

        star_btn = self.wait.until(
            EC.element_to_be_clickable(
                (
                    By.CSS_SELECTOR,
                    "button.v-btn svg path[d*='M9.5,3A6.5,6.5']",
                )
            )
        )
        star_btn.click()

    @allure.step("Перейти в раздел 'Избранное'")
    def go_to_favorites(self) -> None:
        # Переход в избранное (можно через меню профиля или прямой URL)
        profile_menu = self.wait.until(
            EC.element_to_be_clickable(
                (By.CSS_SELECTOR, ".user-avatar, .v-avatar")
            )
        )
        profile_menu.click()
        fav_link = self.wait.until(
            EC.element_to_be_clickable(
                (By.XPATH, "//a[contains(@href, 'favorites') or contains(text(), 'Избранное')]")
            )
        )
        fav_link.click()

    @allure.step("Выйти из аккаунта (логаут)")
    def logout(self) -> None:
        # Открытие меню профиля (иконка аватара или профиля)
        profile_menu = self.wait.until(
            EC.element_to_be_clickable(
                (By.CSS_SELECTOR, ".user-avatar, .v-avatar")
            )
        )
        profile_menu.click()

        # Кнопка «Выход» на основе найденного элемента v-list-item-title из разметки
        logout_btn = self.wait.until(
            EC.element_to_be_clickable((
                    By.XPATH,
                    "//div[contains(@class, 'v-list-item-title') and text()='Выход']",
                )
            )
        )
        logout_btn.click()
