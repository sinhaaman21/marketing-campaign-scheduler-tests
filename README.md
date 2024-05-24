# Marketing Campaign Scheduling Feature Tests

## Setup

### Clone the Repository
git clone https://github.com/sinhaaman21/marketing-campaign-scheduler-tests.git

### Install Dependencies
pip install -r requirements.txt

### Run Mock API Server
python mock_apis/server.py

## Running Tests

### Run All Tests
./scripts/run_tests.sh

### Run Functional Tests
pytest tests/test_functional.py

### Run Integration Tests
pytest tests/test_integration.py

### Run UI Tests
pytest tests/test_ui.py
