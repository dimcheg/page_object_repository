from .base_page import BasePage
from .locators import ProductPageLocators
from selenium.webdriver.common.by import By

class ProductPage(BasePage):
    def should_be_product_page(self):
        self.should_be_add_to_basket_button()
        self.should_be_add_to_wishlist_button()
        self.should_be_write_review_button()

    def add_to_basket(self):
       add_to_basket = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET)
       add_to_basket.click()

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
       "Success message is presented, but should not be"

    def should_be_success_message_disappeared(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), \
       "Success message is presented, but should be disappeare"

    def should_be_correct_added(self):
        self.should_be_correct_name()

    def should_be_add_to_basket_button(self):
        assert self.is_element_present(*ProductPageLocators.ADD_TO_BASKET), 'Button "Add to basket" doesn\'t exist'

    def should_be_add_to_wishlist_button(self):
        assert self.is_element_present(*ProductPageLocators.ADD_TO_WISHLIST), 'Button "Add to wishlist" doesn\'t exist'

    def should_be_write_review_button(self):
        assert self.is_element_present(*ProductPageLocators.WRITE_REVIEW), 'Button "Write review" doesn\'t exist'

    def should_be_correct_added(self):
        assert self.browser.find_element(*ProductPageLocators.BOOK_NAME).text ==\
         self.browser.find_element(*ProductPageLocators.BOOK_NAME_ADDED).text, 'Wrong book added'
        assert self.browser.find_element(*ProductPageLocators.BOOK_PRICE).text ==\
         self.browser.find_element(*ProductPageLocators.BASKET_PRICE).text, 'Wrong book price'
