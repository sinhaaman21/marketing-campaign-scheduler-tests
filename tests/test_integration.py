import pytest
import requests
import requests_mock

class TestCampaignSchedulerIntegration:

    base_url = "http://localhost:5000/api"

    def test_integration_with_recipient_service(self, requests_mock):
        recipient_url = f"{self.base_url}/recipients"
        requests_mock.get(recipient_url, json={"recipients": ["test@example.com"]})
        
        response = requests.get(recipient_url)
        assert response.status_code == 200
        assert response.json() == {"recipients": ["test@example.com"]}

    def test_integration_with_template_service(self, requests_mock):
        template_url = f"{self.base_url}/templates/template_123"
        requests_mock.get(template_url, json={"id": "template_123", "content": "Sample Template"})
        
        response = requests.get(template_url)
        assert response.status_code == 200
        assert response.json() == {"id": "template_123", "content": "Sample Template"}

    def test_scheduling_and_sending_emails(self, requests_mock):
        send_email_url = f"{self.base_url}/send"
        requests_mock.post(send_email_url, json={"status": "sent"})
        
        response = requests.post(send_email_url, json={"campaign_id": 1})
        assert response.status_code == 200
        assert response.json() == {"status": "sent"}
