from .base_page import BasePage
from selenium.webdriver.common.by import By
from .locators import ProductPageLocators
from selenium.common.exceptions import NoAlertPresentException

class ProductPage(BasePage):
    #метод-проверка что существует кнопка добавления в корзину
    def should_be_basket_button(self):
        assert self.is_element_present(*ProductPageLocators.BASKET_BUTTON), "Basket button is not presented"

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), "Success message is presented, but should not be"

    def should_be_desappeared(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), "Success message is desapeared, but should not be"

    #метод для сравнения названия продукта, добавленного в корзину, с названием продукта
    #НЕ РАБОТАЕТ
    def should_be_equal_handle_in_success_message(self):
        expected_handle = self.browser.find_element(*ProductPageLocators.HANDLE_MESSAGE)
        product_handle = self.browser.find_element(*ProductPageLocators.PRODUCT_HANDLE)
        assert exprcted_handle.find(product_handle.text), "Product handle is not equal"

    #метод для сравнения названия продукта, добавленного в корзину, с названием продукта
    # НЕ РАБОТАЕТ
    def should_be_equal_price_in_success_message(self):
        expected_price = self.browser.find_element(*ProductPageLocators.PRICE_MESSAGE)
        product_price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE)
        assert exprcted_price.find(product_price.text), "Product price is not equal"

    #метод добавления в корзину
    def add_to_basket(self):
        basket_button = self.browser.find_element(*ProductPageLocators.BASKET_BUTTON)
        basket_button.click()
    
    #метод для нахождения на странице названия продукта
    #def find_product_handle(self):
        #product_handle = self.browser.find_element(*ProductPageLocators.PRODUCT_HANDLE)
        #expected_handle = product_handle.text
        #return product_handle.text

    #метод для нахождения на странице цены продукта
    #def find_product_price(self):
        #product_price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE)
        #expected_price = product_price.text
        #return product_price.text




    
