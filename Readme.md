**OrangeHRM Automation Testing Project**



Overview

This project automates the testing of the OrangeHRM application using Selenium WebDriver and Python. It covers multiple modules including Login, Leave, Recruitment, PIM, My Info, and Time. The tests are designed using PyTest with a Page Object Model (POM) architecture for maintainability and scalability.



**Project Structure**



orangehrm\_automation/

│

├── config/

│   ├── config.yaml              # URLs, credentials

│   └── test\_data.xlsx           # Data for data-driven tests

│

├── pages/                       # Page Object Model classes

│   ├── login\_page.py

│   ├── leave\_page.py

│   ├── recruitment\_page.py

│   ├── pim\_page.py

│   ├── myinfo\_page.py

│   └── time\_page.py

│

├── tests/                       # PyTest test cases

│   ├── test\_login.py

│   ├── test\_leave.py

│   ├── test\_recruitment.py

│   ├── test\_pim.py

│   ├── test\_myinfo.py

│   └── test\_time.py

│

├── utilities/

│   ├── driver\_factory.py        # WebDriver setup

│   ├── logger.py                # Logging setup

│   ├── excel\_reader.py          # Excel data reading

│   └── screenshot.py            # Screenshot utility

│

├── reports/                     # HTML/Allure reports and screenshots

├── requirements.txt             # Python dependencies

├── pytest.ini                   # PyTest configuration

├── conftest.py                  # PyTest fixtures (setup/teardown)

└── README.md                    # Project documentation





**Modules Covered**

Login Module – Validates login functionality and credentials.



Leave Module – Apply leave, leave entitlement, leave balance, and leave list verification.



Recruitment Module – Add candidate, shortlist, schedule interviews, hire, delete, and manage vacancies.



PIM Module – Employee management, personal details, job details, and reporting.



My Info Module – Personal, contact, emergency contacts, dependents, immigration, job, salary, tax, qualifications, attachments, and profile picture.



Time Module – Attendance punch in/out, timesheet submission, approval, and validation.





**Technologies \& Tools**

Python 3.x



Selenium WebDriver



PyTest for test execution



Excel (openpyxl) for test data



YAML (PyYAML) for configuration



ChromeDriver for browser automation



pytest-html for reports





**Project Features**

Page Object Model (POM) for maintainability



Data-driven testing using Excel



Logging of test execution



Screenshots captured on failure



Modular test organization by OrangeHRM modules



**Author**

Omkar Sanas – QA Automation Engineer











