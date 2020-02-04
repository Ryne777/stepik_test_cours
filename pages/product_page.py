from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def should_be_add_basket_buttom(self):
        assert self.is_element_present(
            *ProductPageLocators.ADD_TO_BASKET_BUTTOM), "not have buttom to add basket"

    def add_to_basket(self):
        add_buttom = self.browser.find_element(
            *ProductPageLocators.ADD_TO_BASKET_BUTTOM)
        add_buttom.click()
        self.solve_quiz_and_get_code()

    def should_be_product_in_basket(self):
        assert self.browser.find_element(*ProductPageLocators.PRODUCT_NAME_IN_BASKET).text == self.browser.find_element(
            *ProductPageLocators.PRODUCT_NAME).text, "difirent product in basket and page"

    def should_be_price_in_basket(self):
        price = self.browser.find_element(*ProductPageLocators.PRICE).text
        priceInBasket = self.browser.find_element(
            *ProductPageLocators.PRICE_IN_BASKET).text
        assert price == priceInBasket, "difirent price in basket and page"
