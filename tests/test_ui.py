from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import pytest
## used dummy selectors for below tests
class TestCampaignSchedulerUI:

    @pytest.fixture(scope="class")
    def setup(self, request):
        # Set up options for different browsers and devices
        options = Options()
        options.add_argument("--headless")
        options.add_argument("--window-size=1920,1080")

        # Initialize browser driver
        self.driver = webdriver.Chrome(options=options)
        
        # initialize different browsers for tests
        # webdriver.Firefox()  # for Firefox
        # webdriver.Safari()   # for Safari
        # webdriver.Edge()     # for Edge

        # mobile emulation
        mobile_emulation = {
            "deviceName": "iPhone X"
        }
        options.add_experimental_option("mobileEmulation", mobile_emulation)
        self.mobile_driver = webdriver.Chrome(options=options)

        # tablet emulation
        tablet_emulation = {
            "deviceName": "iPad"
        }
        options.add_experimental_option("mobileEmulation", tablet_emulation)
        self.tablet_driver = webdriver.Chrome(options=options)

        yield
        self.driver.quit()
        self.mobile_driver.quit()
        self.tablet_driver.quit()

    def test_create_campaign_ui(self, setup):
        self.driver.get("http://localhost:3000")  # dummy URL
        self.driver.find_element(By.ID, "create-campaign").click()
        self.driver.find_element(By.ID, "campaign-name").send_keys("Test Campaign")
        self.driver.find_element(By.ID, "send-time").send_keys("2024-06-01T10:00:00Z")
        self.driver.find_element(By.ID, "save-campaign").click()
        assert "Campaign Created" in self.driver.page_source

    def test_select_recipient_list_ui(self, setup):
        self.driver.get("http://localhost:3000") # dummy URL
        self.driver.find_element(By.ID, "select-recipients").click()
        self.driver.find_element(By.ID, "recipient-list").send_keys("test@example.com")
        self.driver.find_element(By.ID, "save-recipients").click()
        assert "Recipients Saved" in self.driver.page_source

    def test_choose_email_template_ui(self, setup):
        self.driver.get("http://localhost:3000") # dummy URL
        self.driver.find_element(By.ID, "select-template").click()
        self.driver.find_element(By.ID, "template-id").send_keys("template_123")
        self.driver.find_element(By.ID, "save-template").click()
        assert "Template Saved" in self.driver.page_source

    def test_view_and_edit_campaign_ui(self, setup):
        self.driver.get("http://localhost:3000") # dummy URL
        self.driver.find_element(By.ID, "view-campaigns").click()
        self.driver.find_element(By.ID, "campaign-1").click()
        self.driver.find_element(By.ID, "edit-campaign").click()
        self.driver.find_element(By.ID, "campaign-name").clear()
        self.driver.find_element(By.ID, "campaign-name").send_keys("Updated Campaign Name")
        self.driver.find_element(By.ID, "save-campaign").click()
        assert "Campaign Updated" in self.driver.page_source

    def test_cancel_campaign_ui(self, setup):
        self.driver.get("http://localhost:3000") # dummy URL
        self.driver.find_element(By.ID, "view-campaigns").click()
        self.driver.find_element(By.ID, "campaign-1").click()
        self.driver.find_element(By.ID, "cancel-campaign").click()
        assert "Campaign Canceled" in self.driver.page_source

    # mobile compatibility tests
    def test_create_campaign_ui_mobile(self, setup):
        self.mobile_driver.get("http://localhost:3000") # dummy URL
        self.mobile_driver.find_element(By.ID, "create-campaign").click()
        self.mobile_driver.find_element(By.ID, "campaign-name").send_keys("Test Campaign")
        self.mobile_driver.find_element(By.ID, "send-time").send_keys("2024-06-01T10:00:00Z")
        self.mobile_driver.find_element(By.ID, "save-campaign").click()
        assert "Campaign Created" in self.mobile_driver.page_source

    # tablet compatibility tests
    def test_create_campaign_ui_tablet(self, setup):
        self.tablet_driver.get("http://localhost:3000") # dummy URL
        self.tablet_driver.find_element(By.ID, "create-campaign").click()
        self.tablet_driver.find_element(By.ID, "campaign-name").send_keys("Test Campaign")
        self.tablet_driver.find_element(By.ID, "send-time").send_keys("2024-06-01T10:00:00Z")
        self.tablet_driver.find_element(By.ID, "save-campaign").click()
        assert "Campaign Created" in self.tablet_driver.page_source
