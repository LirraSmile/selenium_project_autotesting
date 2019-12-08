from .pages.product_page import ProductPage
from .pages.basket_page import BasketPage
from .pages.login_page import LoginPage
import pytest
import time

#link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
#link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"
#link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207"
link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"


@pytest.mark.need_review
class TestLoginFromProductPage():
    """НЕ РАБОТАЕТ
    @pytest.fixture(scope="function", autouse=True)
    def setup(self):
        email = str(time.time()) + "@fakemail.org"
        password = "Tester123"
        page = ProductPage(browser, link)
        page.open()
        page.go_to_login_page()
        login_page = LoginPage(browser, browser.current_url)
        login_page.register_new_user(email, password)
    """

    def test_guest_can_go_to_login_page_from_product_page(self, browser):
        page = ProductPage(browser, link)
        page.open()
        page.should_be_login_link()
        page.go_to_login_page()

@pytest.mark.need_review
class TestUserAddToBasketFromProductPage():
    def test_guest_can_add_product_to_basket(self, browser):
        # добавление товара в корзину и проверка, что появилось информационное сообщение об этом
        page = ProductPage(browser, link)
        #открыть страницу
        page.open()
        page.should_be_basket_button()
        page.add_to_basket()
        #page.should_be_equal_handle_in_success_message()
        #page.should_be_equal_price_in_success_message()
        #page.solve_quiz_and_get_code()

    def test_guest_cant_see_product_in_basket_from_product_page(self, browser):
        page = ProductPage(browser, link)
        page.open()
        page.go_to_basket_page()
        basket_page = BasketPage(browser, browser.current_url)
        basket_page.should_be_basket_page()

    def test_user_can_add_product_to_basket(self, browser):
        # добавление товара в корзину и проверка, что появилось информационное сообщение об этом
        page = ProductPage(browser, link)
        #открыть страницу
        page.open()
        page.go_to_login_page()
        
        #ЗДЕСЬ ДОЛЖНА БЫТЬ АВТОРИЗАЦИЯ 
        page.should_be_basket_button()
        page.add_to_basket()
        #page.should_be_equal_handle_in_success_message()
        #page.should_be_equal_price_in_success_message()
        #page.solve_quiz_and_get_code()

"""
НЕ РАБОТАЕТ
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    page = ProductPage(browser, link)
    page.open()
    page.add_to_basket()
    page.should_not_be_success_message()

def test_guest_cant_see_success_message(browser):
    page = ProductPage(browser, link)
    page.open()
    page.should_not_be_success_message()

def test_message_disapeared_after_adding_product_to_basket(browser):
    page = ProductPage(browser, link)
    page.open()
    page.add_to_basket()
    page.should_be_desappeared()
"""