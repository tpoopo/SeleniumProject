from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from configparser import ConfigParser
from pages import *


class TestSauceDemo:
    @classmethod
    def setup_class(cls):
        config_data = ConfigParser()
        config_data.read('config.ini')
        try:
            cls.user_name = config_data["SAUCEDEMO_SETTINGS"]["user_name"]
            cls.password = config_data["SAUCEDEMO_SETTINGS"]["password"]
            cls.url = config_data["SAUCEDEMO_SETTINGS"]["url"]
            cls.headless = config_data["SAUCEDEMO_SETTINGS"]["headless"]
            cls.exec_path = config_data["SAUCEDEMO_SETTINGS"]["exec_path"]
        except KeyError as e:
            print("Unable to get configurations from config.ini file: %s" % e)
            exit(-1)
        cls.cart_url = cls.url + "/cart.html"
        options = Options()
        if cls.headless == "True":
            options.headless = True
        cls.driver = webdriver.Firefox(options=options, executable_path=cls.exec_path)
        cls.driver.get(cls.url)

    def test_add_to_cart(self):
        login_page = LoginPage(self.driver)
        store_page = login_page.login(self.user_name, self.password)
        #TODO get test items from config
        test_items = ["Sauce Labs Onesie", "Sauce Labs Bike Light"]
        for test in test_items:
            store_page.addItemToCart(test)
        cart_page = StoreCartPage(self.driver, self.cart_url)
        cart_page.get_url()
        elements = cart_page.getCartElements()
        for test in test_items:
            match = False
            for e in elements:
                if e.find_element_by_class_name("inventory_item_name").text == test:
                    match = True
            assert match, "FAIL: Did not find %s in shopping cart items" % test

    @classmethod
    def teardown_class(self):
        self.driver.close()


def main():
    test_runner = TestSauceDemo()
    test_runner.test_add_to_cart()


if __name__ == "__main__":
    main()
