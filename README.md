# Pytest Framework

This Framework is developed for general usage in any project which use Pytest Framework for Testing UI using Selenium with Python.

## Project By
- @Sanket

## Key Features

Framework is developed using Page object model and Pytest framework. Framework is based on 4 packages as below

- **configuration**
    - config.ini file contains all pre-requisite data


- **generic**
    - property Manager - Reads data from config file
    - Wrapper Function contains all reusable methods and xpaths
    - fileFunctionUtil Contains pure python logical codes
  


- **pageFactory**
    - contains separate pages for each module in which business logic for that module is written
    


- **testCases**
    - conftest.py - It is where you setup test configurations and store the testcases that are used by test functions. The configurations and the testcases are called fixture in pytest.
    - test_filename.py The test_*. py files are where the actual test functions reside.

## Running Tests
- **System setup**
    - configure allure into your system by adding allure path to environment system variable
    - setup a virtual environment for this project
    - install all dependencies from requirement.txt with the help of following command
```bash
    pip install -U -r requirements.txt
```


- **To run test cases**

```bash
    pytest test_filename.py
```
## Reporting
Framework is integrated with Allure reports. To run tests and generate report, run the following command
```bash
    pytest testFileName --alluredir=AllureDirectoryPath
```
e.g  pytest -s -v .\testCases\DemoBlazeEndToEndFlow_Test.py --alluredir=AllureReport\TestReport

-this will create report in json format in specified allure directory
Go to Allure Directory
run the following command to convert it into Allure report 
```bash
    allure serve AllureDirectoryPath
```
e.g  allure serve .\AllureReport\TestReport\


run the following command to execute test in sequential mode with printing statement and more verbosity
```bash
    pytest -s -v .\testCases\DemoBlazeEndToEndFlow_Test.py
```
