from .base_page import BasePage
from .locators import BasketPageLocators

class BasketPage(BasePage):
    def basket_is_empty(self):
        assert self.is_not_element_present(*BasketPageLocators.ITEMS), "Basket is not empty, but should be"
        assert self.is_element_present(*BasketPageLocators.EMPTY_BASKET_TEXT), "Should be message about empty basket"
