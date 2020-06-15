import pytest
from pages.product_page import ProductPage
from pages.login_page import LoginPage
from pages.basket_page import BasketPage
import time
@pytest.mark.parametrize('link',
                             ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0",
                              "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1",
                              "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2",
                              "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer3",
                              "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer4",
                              "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer5",
                              "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6",
                              pytest.param("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7", marks=pytest.mark.xfail),
                              "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer8",
                              "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9"])
@pytest.mark.need_review
def test_guest_can_add_product_to_basket(browser, link):
    link = f"{link}"
    page = ProductPage(browser, link)  # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адр
    page.open()  # открываем страницу
    page.add_to_basket()
    page.solve_quiz_and_get_code()
    time.sleep(1)
    page.should_be_message_about_adding()
    page.should_be_message_basket_total()

def test_guest_cant_see_success_message(browser):
    link = "http://selenium1py.pythonanywhere.com/ru/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    page = ProductPage(browser,
                       link)  # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
    page.open()  # открываем страницу
    time.sleep(1)
    page.should_not_be_success_message()

@pytest.mark.xfail(reason="fixing this bug right now")
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/ru/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    page = ProductPage(browser,
                       link)  # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
    page.open()  # открываем страницу
    page.add_to_basket()
    page.solve_quiz_and_get_code()
    time.sleep(1)
    page.should_not_be_success_message()

@pytest.mark.xfail(reason="fixing this bug right now")
def test_message_disappeared_after_adding_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/ru/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    page = ProductPage(browser, link)  # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
    page.open()  # открываем страницу
    page.add_to_basket()
    page.solve_quiz_and_get_code()
    time.sleep(1)
    page.success_message_should_disappear()

def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()

@pytest.mark.need_review
def test_guest_can_go_to_login_page_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_login_page()

@pytest.mark.need_review
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = BasketPage(browser, link)  # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
    page.open()
    page.go_to_basket()
    page.basket_should_not_have_items()
    page.basket_should_be_empty()

class TestUserAddToBasketFromProductPage():
    @pytest.fixture(scope="function", autouse=True)
    def setup(self,browser):
        link = "http://selenium1py.pythonanywhere.com/ru/catalogue/the-shellcoders-handbook_209/?promo=newYear"
        page = LoginPage(browser, link)
        page.open()
        page.go_to_login_page()
        email = str(time.time()) + "@fakemail.org"
        password = "bitrna5221"
        page.register_new_user(email, password)
        page.should_be_authorized_user()
    def test_user_cant_see_success_message(self, browser):
        link = "http://selenium1py.pythonanywhere.com/ru/catalogue/the-shellcoders-handbook_209/?promo=newYear"
        page = ProductPage(browser, link)  # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
        page.open()  # открываем страницу
        time.sleep(1)
        page.should_not_be_success_message()

    @pytest.mark.need_review
    def test_user_can_add_product_to_basket(self,browser):
        link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0"
        page = ProductPage(browser, link)  # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
        page.open()  # открываем страницу
        page.add_to_basket()
        page.solve_quiz_and_get_code()
        time.sleep(1)
        page.should_be_message_about_adding()
        page.should_be_message_basket_total()


