from .base_page import BasePage
from .locators import LoginPageLocators

class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        # реализуйте проверку на корректный url адрес
        page_url = self.browser.current_url
        #assert self.is_element_present(), "Login link is not expected"
        assert page_url.find("login"), "Login link is not expected"

    def should_be_login_form(self):
        # реализуйте проверку, что есть форма логина
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form is not presented"
        #assert True

    def should_be_register_form(self):
        # реализуйте проверку, что есть форма регистрации на странице
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), "Register form is not presented"
        #assert True

    def register_new_user(self, email, password):
        new_user_email = self.browser.find_element(*LoginPageLocators.REG_EMAIL)
        new_user_email.send_keys(email)
        new_user_password1 = self.browser.find_element(*LoginPageLocators.REG_PASSWORD1)
        new_user_password1.send_keys(password)
        new_user_password2 = self.browser.find_element(*LoginPageLocators.REG_PASSWORD2)
        new_user_password2.send_keys(password)
        button_reg_new_user = self.browser.find_element(*LoginPageLocators.REG_BUTTON)
        button_reg_new_user.click()
