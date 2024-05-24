#!/bin/bash
# Install dependencies
pip install -r requirements.txt
# Run functional tests
pytest tests/test_functional.py
# Run integration tests
pytest tests/test_integration.py
# Run UI tests
pytest tests/test_ui.py