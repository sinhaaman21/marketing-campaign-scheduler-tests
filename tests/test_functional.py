import pytest
import requests

class TestCampaignScheduler:
    
    base_url = "http://localhost:5000/api"

    def test_create_campaign(self):
        response = requests.post(f"{self.base_url}/campaigns", json={
            "name": "Test Campaign",
            "send_time": "2024-06-01T10:00:00Z"
        })
        assert response.status_code == 201
        assert response.json()["id"] is not None

    def test_select_recipient_list(self):
        response = requests.post(f"{self.base_url}/recipients", json={
            "campaign_id": 1,
            "recipients": ["test@example.com"]
        })
        assert response.status_code == 200
        assert response.json()["status"] == "success"

    def test_choose_email_template(self):
        response = requests.post(f"{self.base_url}/templates", json={
            "campaign_id": 1,
            "template_id": "template_123"
        })
        assert response.status_code == 200
        assert response.json()["status"] == "success"

    def test_view_campaign_details(self):
        response = requests.get(f"{self.base_url}/campaigns/1")
        assert response.status_code == 200
        assert "name" in response.json()

    def test_edit_campaign(self):
        response = requests.put(f"{self.base_url}/campaigns/1", json={
            "name": "Updated Campaign Name"
        })
        assert response.status_code == 200
        assert response.json()["name"] == "Updated Campaign Name"

    def test_cancel_campaign(self):
        response = requests.delete(f"{self.base_url}/campaigns/1")
        assert response.status_code == 200
        assert response.json()["status"] == "canceled"
