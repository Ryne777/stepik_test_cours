from .base_page import BasePage
from .locators import BasketPageLocators

class BasketPage(BasePage):
    def should_not_be_basket_items(self):
        assert self.is_not_element_present(*BasketPageLocators.PRODUCT_IN_BASKET), \
            "Success message is presented, but should not be"

    def should_be_basket_empty_masseng(self):
        assert self.is_element_present(
            *BasketPageLocators.MASSENG_IN_BOTTOM), "not have masseng"
