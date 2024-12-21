from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from features.pages.base_page_object import BasePage

class DashboardPage(BasePage):
    DASHBOARD_LABEL = By.XPATH, "//h6[contains(text(),'Dashboard')]"

    def __init__(self, context):
        BasePage.__init__(
            self,
            context.browser
            # base_url='https://opensource-demo.orangehrmlive.com/web/index.php/dashboard/index'
        )

    def verify_label(self, text):
        wait = WebDriverWait(self, 10)
        dashboard_element = wait.until(EC.visibility_of_element_located(self.DASHBOARD_LABEL))
        assert text in dashboard_element.text