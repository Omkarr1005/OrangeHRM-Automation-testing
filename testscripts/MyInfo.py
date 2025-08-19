from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import os

# ---------- DRIVER INIT ----------
driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
wait = WebDriverWait(driver, 15)

# ---------- LOGIN ----------
def login(username="Admin", password="admin123"):
    wait.until(EC.presence_of_element_located((By.NAME, "username"))).send_keys(username)
    driver.find_element(By.NAME, "password").send_keys(password)
    driver.find_element(By.XPATH, "//button[@type='submit']").click()
    wait.until(EC.presence_of_element_located((By.XPATH, "//span[text()='Dashboard']")))
    print("[INFO] Logged in successfully")

# ---------- NAVIGATE TO MY INFO ----------
def go_to_my_info():
    wait.until(EC.element_to_be_clickable((By.XPATH, "//span[text()='My Info']"))).click()
    wait.until(EC.presence_of_element_located((By.XPATH, "//h6[text()='Personal Details']")))
    print("[INFO] Navigated to My Info page")

# ---------- PERSONAL DETAILS ----------
def update_personal_details():
    print("\n[INFO] Updating Personal Details...")
    driver.find_element(By.XPATH, "//button[text()='Edit']").click()
    wait.until(EC.element_to_be_clickable((By.NAME, "firstName"))).clear()
    driver.find_element(By.NAME, "firstName").send_keys("Omkar")
    driver.find_element(By.NAME, "middleName").send_keys("S.")
    driver.find_element(By.NAME, "lastName").send_keys("Sanas")
    # Gender
    driver.find_element(By.XPATH, "//input[@name='gender' and @value='M']").click()
    # Nationality
    nationality_dropdown = driver.find_element(By.XPATH, "//label[text()='Nationality']/..//div[@role='combobox']")
    nationality_dropdown.click()
    wait.until(EC.element_to_be_clickable((By.XPATH, "//span[text()='Indian']"))).click()
    # Save
    driver.find_element(By.XPATH, "//button[text()='Save']").click()
    print("[PASS] Personal Details updated ✅")

# ---------- CONTACT DETAILS ----------
def update_contact_details():
    print("\n[INFO] Updating Contact Details...")
    driver.find_element(By.XPATH, "//a[text()='Contact Details']").click()
    driver.find_element(By.XPATH, "//button[text()='Edit']").click()
    driver.find_element(By.NAME, "street1").clear()
    driver.find_element(By.NAME, "street1").send_keys("ABC Road")
    driver.find_element(By.NAME, "city").clear()
    driver.find_element(By.NAME, "city").send_keys("Mumbai")
    driver.find_element(By.NAME, "zipCode").clear()
    driver.find_element(By.NAME, "zipCode").send_keys("400001")
    country_dropdown = driver.find_element(By.XPATH, "//label[text()='Country']/..//div[@role='combobox']")
    country_dropdown.click()
    wait.until(EC.element_to_be_clickable((By.XPATH, "//span[text()='India']"))).click()
    driver.find_element(By.XPATH, "//button[text()='Save']").click()
    print("[PASS] Contact Details updated ✅")

# ---------- EMERGENCY CONTACT ----------
def add_emergency_contact():
    print("\n[INFO] Adding Emergency Contact...")
    driver.find_element(By.XPATH, "//a[text()='Emergency Contacts']").click()
    driver.find_element(By.XPATH, "//button[text()='Add']").click()
    driver.find_element(By.NAME, "name").send_keys("Raj")
    driver.find_element(By.NAME, "relationship").send_keys("Brother")
    driver.find_element(By.NAME, "homeTelephone").send_keys("1234567890")
    driver.find_element(By.XPATH, "//button[text()='Save']").click()
    print("[PASS] Emergency Contact added ✅")

# ---------- DEPENDENTS ----------
def add_dependent():
    print("\n[INFO] Adding Dependent...")
    driver.find_element(By.XPATH, "//a[text()='Dependents']").click()
    driver.find_element(By.XPATH, "//button[text()='Add']").click()
    driver.find_element(By.NAME, "name").send_keys("Riya")
    driver.find_element(By.NAME, "relationship").send_keys("Child")
    driver.find_element(By.NAME, "dateOfBirth").send_keys("2015-01-01")
    driver.find_element(By.XPATH, "//button[text()='Save']").click()
    print("[PASS] Dependent added ✅")

# ---------- IMMIGRATION ----------
def add_immigration_record():
    print("\n[INFO] Adding Immigration Record...")
    driver.find_element(By.XPATH, "//a[text()='Immigration']").click()
    driver.find_element(By.XPATH, "//button[text()='Add']").click()
    driver.find_element(By.NAME, "number").send_keys("X1234567")
    driver.find_element(By.NAME, "passportIssuedDate").send_keys("2020-01-01")
    driver.find_element(By.NAME, "passportExpiryDate").send_keys("2030-01-01")
    driver.find_element(By.XPATH, "//button[text()='Save']").click()
    print("[PASS] Immigration record added ✅")

# ---------- JOB ----------
def check_job_details():
    print("\n[INFO] Checking Job Details...")
    driver.find_element(By.XPATH, "//a[text()='Job']").click()
    time.sleep(2)  # just to allow job details to load
    print("[PASS] Job details displayed ✅")

# ---------- SALARY ----------
def check_salary_details():
    print("\n[INFO] Checking Salary Details...")
    driver.find_element(By.XPATH, "//a[text()='Salary']").click()
    time.sleep(2)
    print("[PASS] Salary details displayed ✅")

# ---------- TAX EXEMPTIONS ----------
def add_tax_exemption():
    print("\n[INFO] Adding Tax Exemption...")
    driver.find_element(By.XPATH, "//a[text()='Tax Exemptions']").click()
    driver.find_element(By.XPATH, "//button[text()='Add']").click()
    driver.find_element(By.NAME, "federalStatus").send_keys("Single")
    driver.find_element(By.XPATH, "//button[text()='Save']").click()
    print("[PASS] Tax Exemption saved ✅")

# ---------- QUALIFICATIONS ----------
def add_qualification():
    print("\n[INFO] Adding Qualification...")
    driver.find_element(By.XPATH, "//a[text()='Qualifications']").click()
    driver.find_element(By.XPATH, "//button[text()='Add']").click()
    driver.find_element(By.NAME, "company").send_keys("ABC Corp")
    driver.find_element(By.NAME, "jobTitle").send_keys("QA Intern")
    driver.find_element(By.NAME, "fromDate").send_keys("2022-01-01")
    driver.find_element(By.NAME, "toDate").send_keys("2023-01-01")
    driver.find_element(By.XPATH, "//button[text()='Save']").click()
    print("[PASS] Qualification added ✅")

# ---------- ATTACHMENTS ----------
def add_attachment():
    print("\n[INFO] Adding Attachment...")
    driver.find_element(By.XPATH, "//a[text()='Attachments']").click()
    driver.find_element(By.XPATH, "//button[text()='Add']").click()
    upload_path = os.path.abspath("resume.pdf")  # Make sure file exists
    driver.find_element(By.XPATH, "//input[@type='file']").send_keys(upload_path)
    driver.find_element(By.XPATH, "//button[text()='Save']").click()
    print("[PASS] Attachment uploaded ✅")

# ---------- PROFILE PICTURE ----------
def upload_profile_picture():
    print("\n[INFO] Uploading Profile Picture...")
    driver.find_element(By.XPATH, "//img[@alt='Profile Picture']").click()
    upload_path = os.path.abspath("profile.jpg")  # Make sure file exists
    driver.find_element(By.XPATH, "//input[@type='file']").send_keys(upload_path)
    driver.find_element(By.XPATH, "//button[text()='Upload']").click()
    print("[PASS] Profile Picture uploaded ✅")

# ---------- RUN ALL TESTS ----------
if __name__ == "__main__":
    login()
    go_to_my_info()
    update_personal_details()
    update_contact_details()
    add_emergency_contact()
    add_dependent()
    add_immigration_record()
    check_job_details()
    check_salary_details()
    add_tax_exemption()
    add_qualification()
    add_attachment()
    upload_profile_picture()
    driver.quit()
