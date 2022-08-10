from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


class Keyword_Processor:

    def __init__(self, driver):
        self.element = None
        self.driver = driver

    def keyword_click(self, locator, locator_value, action):
        if action == "click" or action == "Click" or action == "click()" or action == "Click()":

            if locator == "id" or locator == "ID":
                self.element = self.driver.find_element(By.ID, locator_value).click()

            elif locator == "NAME" or locator == 'name':
                self.element = self.driver.find_element(By.NAME, locator_value).click()

            elif locator == "linktext" or locator == 'Linktext' or locator == "LINK_TEXT":
                self.element = self.driver.find_element(By.LINK_TEXT, locator_value).click()
                
            elif locator == "XPATH" or locator == "xpath":
                self.element = self.driver.find_element(By.XPATH, locator_value).click()

    def keyword_sendkeys(self, locator, locator_value, action, action_value):

        if action == "sendkeys" or action == "SENDKEYS" or action == "send_keys" or action == "send_keys()":
            if locator == "id" or locator == "ID":
                self.driver.find_element(By.ID, locator_value).send_keys(action_value)
            elif locator == "NAME" or locator == 'name':
                self.driver.find_element(By.NAME, locator_value).send_keys(action_value)
            elif locator == "NAME" or locator == 'name':
                self.driver.find_element(By.NAME, locator_value).send_keys(action_value)
            elif locator == "xpath" or locator == 'XPATH':
                self.driver.find_element(By.XPATH, locator_value).send_keys(action_value)
            elif locator == "css selector" or locator == 'CSS_SELECTOR':
                self.driver.find_element(By.CSS_SELECTOR, locator_value).send_keys(action_value)
    
    def keyword_class(self, locator, locator_value, action, action_value, class_name):

        if class_name == "select" or class_name == "Select" or class_name == "SELECT" or class_name == "Select()":
            if action == "select_by_visible_text" or action == "selectbyvisibletext" or \
                    action == "select by visible text" or action == "Select by visible text":
                if locator == "xpath" or locator == 'XPATH':
                    Select(self.driver.find_element(By.XPATH, locator_value)).select_by_visible_text(action_value)
            elif action == "select_by_value" or action == "selectbyvalue" or action == "select by value" or\
                    action == "Select by value":
                if locator == "xpath" or locator == 'XPATH':
                    Select(self.driver.find_element(By.XPATH, locator_value)).select_by_value(action_value)
            elif action == "select_by_index" or action == "selectbyindex" or action == "select by index" or \
                    action == "Select by index":
                if locator == "xpath" or locator == 'XPATH':
                    Select(self.driver.find_element(By.XPATH, locator_value)).select_by_index(action_value)
