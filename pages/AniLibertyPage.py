import time
import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver


class AniLibertyPages:
    """Класс страниц для проекта AniLiberty"""

    def __init__(self, driver: WebDriver) -> None:
        self.driver = driver

    @allure.step("Открыть главную страницу авторизации AniLiberty")
    def open_home_page(self) -> None:
        self.driver.get("https://www.aniliberty.top/app/auth/login")

    @allure.step("Выполнить авторизацию с логином")
    def login(self, login: str, password: str) -> None:
        login_input = self.driver.find_element(By.NAME, "login")
        login_input.clear()
        login_input.send_keys(login)

        password_input = self.driver.find_element(By.NAME, "current-password")
        password_input.clear()
        password_input.send_keys(password)

        submit_btn = self.driver.find_element(
            By.CSS_SELECTOR, "button.v-btn, button[type='button']"
        )
        submit_btn.click()

        time.sleep(2)

    @allure.step("Кликнуть по иконке лупы для открытия поиска")
    def open_search_modal(self) -> None:
        search_btn = self.driver.find_element(
            By.CSS_SELECTOR,
            "button.v-btn.v-theme--dark.bg-transparent:nth-of-type(2)"
        )
        search_btn.click()

        time.sleep(1)

    @allure.step("Ввести поисковый запрос")
    def search_title(self, query: str) -> None:
        input_field = self.driver.find_element(
            By.CSS_SELECTOR, "input.v-field__input"
        )
        input_field.clear()
        input_field.send_keys(query)

        time.sleep(3)

    @allure.step("Выбрать первый результат из списка поиска "
                 "по внутренней ссылке")
    def open_first_search_result_by_href(self) -> None:
        results = self.driver.find_elements(
            By.CSS_SELECTOR, "a[role='listitem'][href*='/episodes']"
        )

        first_item = results[0]

        link_href = first_item.get_attribute("href")
        print(f"\n---> НАШЛИ ССЫЛКУ В ПОИСКЕ: {link_href}")

        self.driver.get(link_href)
        time.sleep(3)

    @allure.step("Проверить, что кнопка «Смотреть с 1 эпизода» отображается")
    def is_watch_button_displayed(self) -> bool:
        time.sleep(2)
        watch_btn = self.driver.find_element(
            By.CSS_SELECTOR, "a[href*='/anime/video/episode/']"
        )
        return watch_btn.is_displayed()

    @allure.step("Добавить первый релиз в избранное и проверить, "
                 "что звезда стала красной")
    def click_and_check_star_in_catalog(self) -> bool:
        self.driver.get("https://www.aniliberty.top/anime/catalog/")
        time.sleep(3)

        star_selector = "div.v-layout.mt-4 button.v-btn[style*='width: 40px']"

        star_btn = self.driver.find_element(By.CSS_SELECTOR, star_selector)

        if "bg-secondary" in star_btn.get_attribute("class"):
            self.driver.execute_script("arguments[0].click();", star_btn)
            time.sleep(2)
            star_btn = self.driver.find_element(By.CSS_SELECTOR, star_selector)

        self.driver.execute_script("arguments[0].click();", star_btn)
        time.sleep(2)

        updated_star_btn = self.driver.find_element(By.CSS_SELECTOR,
                                                    star_selector)
        return "bg-secondary" in updated_star_btn.get_attribute("class")

    @allure.step("Перейти в раздел 'Избранное'")
    def go_to_favorites(self) -> None:
        profile_menu = self.driver.find_element(
            By.CSS_SELECTOR, ".user-avatar, .v-avatar"
        )
        profile_menu.click()

        time.sleep(1)

        fav_link = self.driver.find_element(
            By.XPATH, "//a[contains(@href, 'favorites') "
            "or contains(text(), 'Избранное')]"
        )
        fav_link.click()

    @allure.step("Выйти из аккаунта")
    def logout(self) -> None:
        profile_menu = self.driver.find_element(
            By.CSS_SELECTOR, ".user-avatar, .v-avatar"
        )
        profile_menu.click()

        time.sleep(3)

        logout_btn = self.driver.find_element(
            By.XPATH,
            "//div[contains(@class, 'v-list-item-title') and text()='Выход']",
        )
        self.driver.execute_script("arguments[0].click();", logout_btn)
