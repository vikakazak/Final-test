from selenium.webdriver.common.by import By

class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "div.login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "div.register_form")
    REGISTER_EMAIL=(By.CSS_SELECTOR, "[name='registration-email']")
    REGISTER_PASSWORD=(By.CSS_SELECTOR, "[name='registration-password1']")
    CONFIRM_PASSWORD = (By.CSS_SELECTOR, "[name='registration-password2']")
    REGISTER_BUTTON= (By.CSS_SELECTOR, "[name='registration_submit']")

class ProductPageLocators():
    ADD_TO_BASKET_BUTTON = (By.CSS_SELECTOR, "button.btn-add-to-basket")
    SUCCESS_MESSAGE=(By.CSS_SELECTOR, "#messages>div:nth-child(1) strong")

class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BASKET_BUTTON = (By.CSS_SELECTOR, "span.btn-group>a")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")

class BasketPageLocators():
    EMPTY_BASKET_MESSAGE=(By.CSS_SELECTOR, "#content_inner>p")
    BASKET_ITEMS=(By.CSS_SELECTOR, "#basket_formset")
