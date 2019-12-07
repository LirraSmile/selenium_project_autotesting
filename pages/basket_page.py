from .base_page import BasePage

class BasketPage(BasePage):
    def should_be_basket_page(self):
        self.should_be_basket_url()
        self.should_be_empty

    def should_be_basket_url(self):
        # реализуйте проверку на корректный url адрес
        page_url = self.browser.current_url
        assert page_url.find("basket"), "Login link is not expected"

    def should_be_empty(self):
        empty_text = self.browser.find_element_by_css_selector(".content > p")
        present_text = empty_text.text
        expected_text = "Your basket is empty"
        assert present_text == expected_text, "Basket is not empty"