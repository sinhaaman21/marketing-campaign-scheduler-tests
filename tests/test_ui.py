from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest
## used dummy selectors for below tests
class TestCampaignSchedulerUI:

    @pytest.fixture(scope="class")
    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.get("http://localhost:3000")  # dummy URL
        yield
        self.driver.quit()

    def test_create_campaign_ui(self, setup):
        self.driver.find_element(By.ID, "create-campaign").click()
        self.driver.find_element(By.ID, "campaign-name").send_keys("Test Campaign")
        self.driver.find_element(By.ID, "send-time").send_keys("2024-06-01T10:00:00Z")
        self.driver.find_element(By.ID, "save-campaign").click()
        assert "Campaign Created" in self.driver.page_source

    def test_select_recipient_list_ui(self, setup):
        self.driver.find_element(By.ID, "select-recipients").click()
        self.driver.find_element(By.ID, "recipient-list").send_keys("test@example.com")
        self.driver.find_element(By.ID, "save-recipients").click()
        assert "Recipients Saved" in self.driver.page_source

    def test_choose_email_template_ui(self, setup):
        self.driver.find_element(By.ID, "select-template").click()
        self.driver.find_element(By.ID, "template-id").send_keys("template_123")
        self.driver.find_element(By.ID, "save-template").click()
        assert "Template Saved" in self.driver.page_source

    def test_view_and_edit_campaign_ui(self, setup):
        self.driver.find_element(By.ID, "view-campaigns").click()
        self.driver.find_element(By.ID, "campaign-1").click()
        self.driver.find_element(By.ID, "edit-campaign").click()
        self.driver.find_element(By.ID, "campaign-name").clear()
        self.driver.find_element(By.ID, "campaign-name").send_keys("Updated Campaign Name")
        self.driver.find_element(By.ID, "save-campaign").click()
        assert "Campaign Updated" in self.driver.page_source

    def test_cancel_campaign_ui(self, setup):
        self.driver.find_element(By.ID, "view-campaigns").click()
        self.driver.find_element(By.ID, "campaign-1").click()
        self.driver.find_element(By.ID, "cancel-campaign").click()
        assert "Campaign Canceled" in self.driver.page_source
