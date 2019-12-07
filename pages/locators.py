from selenium.webdriver.common.by import By

class BasePageLocators():    
    BASKET_BUTTON_DEFAULT = (By.CSS_SELECTOR, ".btn-group > .btn:nth-child(1)")
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
"""
локатор из этого класса перенесен в класс BasePageLocators()
class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
"""
class LoginPageLocators():
    # селекторы к формам регистрации и логина
    LOGIN_FORM = (By.CLASS_NAME, "login_form")
    REGISTER_FORM = (By.CLASS_NAME, "register_form")

class ProductPageLocators():
    # селектор к кнопке добавления товара в корзину
    BASKET_BUTTON = (By.CLASS_NAME, "btn-add-to-basket")
    # СКОРЕЕ ВСЕГО НЕ РАБОТАЮТ
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, "#messages")
    PRODUCT_HANDLE = (By.CSS_SELECTOR, ".product_main h1")
    PRODUCT_PRICE = (By.CSS_SELECTOR, ".product_main p.price_color")
    HANDLE_MESSAGE = (By.CSS_SELECTOR, ".alert.alert-success .alertinner")
    PRICE_MESSAGE = (By.CSS_SELECTOR, ".alert.alert-info .alertinner p")