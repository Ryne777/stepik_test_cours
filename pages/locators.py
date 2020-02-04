from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    RGISTOR_FORM = (By.CSS_SELECTOR, "#register_form")


class ProductPageLocators():
    ADD_TO_BASKET_BUTTOM = (By.CSS_SELECTOR, ".btn-add-to-basket")
    PRICE = (By.CSS_SELECTOR, ".product_main p")
    PRODUCT_NAME = (By.CSS_SELECTOR, ".product_main h1")
    PRODUCT_NAME_IN_BASKET = (By.CSS_SELECTOR, ".alertinner strong")
    PRICE_IN_BASKET = (By.CSS_SELECTOR, ".alert-info div p strong")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, ".alert-success")


class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BASKET_LINK = (By.CSS_SELECTOR, ".btn-group a")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")


class BasketPageLocators():
    MASSENG_IN_BOTTOM = (By.CSS_SELECTOR, "#content_inner p")
    PRODUCT_IN_BASKET = (By.CSS_SELECTOR, ".basket-items")
