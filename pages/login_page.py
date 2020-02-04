from .base_page import BasePage
from .locators import LoginPageLocators
from selenium.webdriver.common.by import By


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        login_url = self.url.split("/")
        assert "login" in login_url, "not login url"

    def should_be_login_form(self):
        # реализуйте проверку, что есть форма логина
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM)

    def should_be_register_form(self):
        # реализуйте проверку, что есть форма регистрации на странице
        assert self.is_element_present(*LoginPageLocators.RGISTOR_FORM)

    def register_new_user(self, email, password):
        self.browser.find_element(
            By.CSS_SELECTOR, "#id_registration-email").send_keys(email)
        self.browser.find_element(
            By.CSS_SELECTOR, "#id_registration-password1").send_keys(password)
        self.browser.find_element(
            By.CSS_SELECTOR, "#id_registration-password2").send_keys(password)
        self.browser.find_element(
            By.CSS_SELECTOR, 'button[value="Register"]').click()
