
# Selenium Python Automation Framework 

This is a sample test automation framework for web application testing using Selenium and Python. It follows the Page Object Model design pattern.
The sample page uses the main DuckDuckGo page
The sample test does a simple search and assert result in page title

## Overview

The framework consists of:

- `/data` - Directory for sorting input test data
- `/logs` - Contains logs from test runs
- `/pages` - Contains the page object classes for application pages
- `/reports` - Stores the test reports
- `/tests` - The test scripts divided into separate classes by functionality


## Setup 

- Clone repository 
- Open in a Python IDE
- Install Python 3.9+
- Install pip
- Install dependencies: `pip install -r requirements.txt` 
- Download web drivers for Chrome and Firefox
- Add web drivers to PATH

## Running Tests

To run all tests:
```
pytest
```

To run specific tests:
```
pytest tests\test_search.py
```


## Reports

HTML reports are to be generated in the `/reports` folder.

