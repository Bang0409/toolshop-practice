from playwright.sync_api import Page
from pages.base_page import BasePage


class LoginPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)

        self.email = page.get_by_test_id("email")
        self.password = page.get_by_test_id("password")
        self.login_button = page.get_by_test_id("login-submit")

        self.login_error = page.get_by_test_id("login-error")
        self.email_error = page.get_by_test_id("email-error")
        self.password_error = page.get_by_test_id("password-error")

    def open(self):
        self.page.goto("/auth/login")
        return self

    def login(self, email: str, password: str):
        self.email.fill(email)
        self.password.fill(password)
        self.login_button.click()
        return self