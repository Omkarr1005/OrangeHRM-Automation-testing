# 🖥️ OrangeHRM Automation Testing Project (Data-Driven, Selenium & Python)

## 📌 Project Overview
This project involved **automation testing** of the OrangeHRM web application using **Selenium WebDriver** and **data-driven testing** in Python.  
Manual test cases from the **OrangeHRM manual testing project** were converted into automated scripts to reduce repetitive testing effort and ensure regression coverage.

## 🎯 Objectives
- Automate pre-defined manual test cases for faster execution.  
- Implement **data-driven testing** to handle multiple test scenarios with different input data.  
- Validate core HR modules and workflows.  
- Generate structured execution reports for test results.

## 🔍 Testing Approach
- **Types of Testing Performed:**
  - Functional Automation Testing
  - Regression Testing
  - Data-Driven Testing using Excel/CSV
  - UI/UX Validation
  - Positive & Negative Test Cases

- **Tools & Libraries Used:**
  - **Selenium WebDriver** – Python for browser automation  
  - **PyTest / Unittest** – Test framework with test reporting  
  - **OpenPyXL / Pandas** – Reading test data from Excel/CSV  
  - **Chrome/Firefox** – Cross-browser testing  
  - **Excel / CSV** – Test data management for data-driven tests  

## ✅ Modules Automated
- **Admin / User Management** – Add, edit, delete users with multiple roles.  
- **Leave Management** – Apply leave, approve/reject leave, leave balance validation.  
- **Time Module** – Submit and validate timesheets and attendance records.  
- **Recruitment Module** – Add candidates, schedule interviews, validate workflow.  
- **My Info Module** – Update employee profile, verify document uploads and personal info.  

## 📝 Sample Data-Driven Test Scenarios

| Module                 | Test Case Description                                | Test Data Source     | Expected Result |
|------------------------|------------------------------------------------------|--------------------|----------------|
| Admin / User Management | Add a new user with multiple roles                  | Excel / CSV        | User created successfully with correct role |
| Leave Management        | Apply leave with different leave types              | Excel / CSV        | Leave application validated correctly |
| Time Module             | Submit timesheet for multiple employees            | Excel / CSV        | Timesheets saved accurately |
| Recruitment Module      | Add multiple candidates and schedule interviews     | Excel / CSV        | Candidate added and interview scheduled |
| My Info Module          | Update personal info with different inputs          | Excel / CSV        | Changes reflected correctly in profile |

## 🐞 Bug & Issue Reporting
- Automation scripts helped detect:
  - Functional discrepancies  
  - Workflow issues  
  - UI/UX inconsistencies  

- All issues were logged with:
  - **Bug ID**
  - **Title/Description**
  - **Steps to Reproduce**
  - **Severity/Priority**
  - **Screenshots / Logs**

## 🚀 Outcome
- Converted manual test cases into **automated scripts**, saving repetitive testing effort.  
- Validated multiple input scenarios using **data-driven testing**, ensuring robust regression coverage.  
- Generated detailed execution reports for review and verification.  
- Strengthened overall QA process for OrangeHRM.

---
👨‍💻 **Tester/Automation Engineer:** Omkar Sanas  
📅 **Duration:** Internship / Personal Project  
🛠️ **Role:** Selenium Automation & Data-Driven Testing Engineer  
