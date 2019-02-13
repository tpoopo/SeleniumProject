class Page(object):
    url = None

    def __init__(self, driver, base_url='https://www.saucedemo.com'):
        self.base_url = base_url
        self.driver = driver
        self.timeout = 60

    def get_url(self):
        self.driver.get(self.base_url)

    def fill_form_by_id(self, id, value):
        element = self.driver.find_element_by_id(id)
        element.send_keys(value)

#    def find_elements_by_class(self, class_name):
#        return self.driver.find_elements_by_class_name(class_name)


class LoginPage(Page):

    def setUser(self, user_name):
        self.fill_form_by_id("user-name", user_name)

    def setPassword(self, password):
        self.fill_form_by_id("password", password)

    def submit(self):
        self.driver.find_element_by_class_name("login-button").click()

    def login(self, user_name, password):
        self.setUser(user_name)
        self.setPassword(password)
        self.submit()
        return StorePage(self.driver)


class StorePage(Page):

    def addItemToCart(self, item):
        elements = self.driver.find_elements_by_class_name("inventory_item")
        for e in elements:
            e_text = e.find_element_by_class_name("inventory_item_name").text
            if e_text == item:
                e.find_element_by_class_name("add-to-cart-button").click()


class StoreCartPage(Page):

    def getCartElements(self):
        return self.driver.find_elements_by_class_name("cart_item")


