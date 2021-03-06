import allure

from pages.internal_page import InternalPage
from pages.internal_pages.dashboard_page import DashboardPage
from pages.internal_pages.main_page import MainPage
from pages.login_window import LoginWindow


class OxwallApp:
    def __init__(self, driver, base_url="http://127.0.0.1/oxwall/"):
        # Open Oxwall UI in browser
        self.driver = driver
        self.driver.implicitly_wait(1)
        self.base_url = base_url
        self.driver.get(self.base_url)

        self._any_internal_page = InternalPage(self.driver)
        self.main_page = MainPage(self.driver)
        self.login_window = LoginWindow(self.driver)
        self.dash_page = DashboardPage(self.driver)

    def close(self):
        self.driver.quit()

    @allure.step("I log as {user}")
    def login(self, user):
        self.main_page.sign_in_link.click()
        username_field = self.login_window.username_field
        username_field.input(user.username)
        password_field = self.login_window.password_field
        password_field.input(user.password)
        self.login_window.click_sing_in_btn()

    @allure.step("WHEN I open a members page")
    def go_to_members_page(self):
        self._any_internal_page.members_link.click()

    @allure.step("I log out")
    def logout(self):
        page = self._any_internal_page
        page.sign_out()

    @allure.step("WHEN I add a new news {news}")
    def add_new_news(self, news):
        news_text_field = self.dash_page.news_text_field
        news_text_field.input(news.text)
        self.dash_page.send_button.click()

    @allure.step("WHEN I wait for a new news appearing")
    def wait_new_news_appearing(self, old_list_of_news):
        #  Wait for new news to appear
        self.dash_page.wait_new_news_appearing()
