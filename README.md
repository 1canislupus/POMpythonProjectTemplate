
# Selenium Python Automation POM Template

This is a sample test automation template for web application testing using Selenium and Python. It follows the Page Object Model design pattern. <br>
The sample page uses the main DuckDuckGo page. <br>
The sample test does a simple search and asserts result in page title. <br>
<br>
You should be able to clone the repository, install dependencies and run the first test. After that, you can add more pages and tests to build your own functional test suite.

## Overview

This repository template consists of:

- `/data` - Directory for sorting input test data
- `/logs` - Contains logs from test runs
- `/pages` - Contains the page object classes for application pages
- `/reports` - Stores the test reports
- `/tests` - The test scripts divided into separate classes by functionality


## Setup 

- Clone repository
- Install Python 3.11+ (older versions potentially compatible)
- Install pip
- Install dependencies: `pip install -r requirements.txt` 
- Download web drivers for Chrome and Firefox
- Add web drivers to PATH

## Running Tests from command line

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

