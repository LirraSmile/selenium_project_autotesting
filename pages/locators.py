from selenium.webdriver.common.by import By

class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
    # селекторы к формам регистрации и логина
    LOGIN_FORM = (By.CLASS_NAME, "login_form")
    REGISTER_FORM = (By.CLASS_NAME, "register_form")

class ProductPageLocators():
    # селектор к кнопке добавления товара в корзину
    BASKET_BUTTON = (By.CLASS_NAME, "btn-add-to-basket")