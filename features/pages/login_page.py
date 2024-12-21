from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from features.pages.base_page_object import BasePage

class LoginPage(BasePage):
    logo_locator = By.CLASS_NAME, "orangehrm-login-branding"
    # username_locator = By.CSS_SELECTOR, "oxd-input.oxd-input--active"
    username_locator = By.NAME, "username"
    password_locator = By.NAME, "password"
    login_button = By.XPATH, "//*[@id='app']/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button"


    def __init__(self, context):
        BasePage.__init__(
            self,
            context.browser,
            base_url='https://opensource-demo.orangehrmlive.com/')

    def type_user(self,username):
        wait = WebDriverWait(self, 10)
        username_element = wait.until(EC.element_to_be_clickable(self.username_locator))
        username_element.send_keys(username)

    def type_password(self,pwd):
        wait = WebDriverWait(self, 10)
        password_element = wait.until(EC.element_to_be_clickable(self.password_locator))
        password_element.send_keys(pwd)

    def click_button(self):
        wait = WebDriverWait(self, 10)
        login_button_element = wait.until(EC.element_to_be_clickable(self.login_button))
        login_button_element.click()
