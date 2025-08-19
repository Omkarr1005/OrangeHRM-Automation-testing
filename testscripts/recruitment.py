from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC
import time
import os

# --- Setup ---
driver = webdriver.Chrome()
driver.maximize_window()
wait = WebDriverWait(driver, 15)

# --- Login ---
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
wait.until(EC.presence_of_element_located((By.NAME, "username"))).send_keys("Admin")
driver.find_element(By.NAME, "password").send_keys("admin123")
driver.find_element(By.XPATH, "//button[@type='submit']").click()

# --- Navigate to Recruitment ---
wait.until(EC.element_to_be_clickable((By.XPATH, "//span[text()='Recruitment']"))).click()

# --- Add Candidate ---
wait.until(EC.element_to_be_clickable((By.XPATH, "//button[normalize-space()='Add']"))).click()

# Fill Candidate details
wait.until(EC.presence_of_element_located((By.NAME, "firstName"))).send_keys("Omkar")
driver.find_element(By.NAME, "middleName").send_keys("Test")
driver.find_element(By.NAME, "lastName").send_keys("Candidate")

# Vacancy dropdown
vacancy_label = wait.until(EC.presence_of_element_located(
    (By.XPATH, "//label[text()='Vacancy']/following::div[contains(@class,'oxd-select-text-input')]")
))
vacancy_label.click()

# Wait and select first vacancy from list
vacancy_option = wait.until(EC.element_to_be_clickable(
    (By.XPATH, "//div[@role='option'][1]")
))
vacancy_option.click()

# Email & contact
driver.find_element(By.XPATH, "//label[text()='Email']/following::input[1]").send_keys("test@example.com")
driver.find_element(By.XPATH, "//label[text()='Contact Number']/following::input[1]").send_keys("9876543210")

# Resume upload
resume_path = r"C:\Users\Omkar\Documents\resume.pdf"
if not os.path.exists(resume_path):
    print("⚠ Resume not found, create dummy file for test.")
    with open(resume_path, "w") as f:
        f.write("Dummy resume content.")
driver.find_element(By.XPATH, "//input[@type='file']").send_keys(resume_path)
# Tick the "Consent to keep data" checkbox
consent_checkbox = wait.until(EC.element_to_be_clickable(
    (By.XPATH, "//label[text()='Consent to keep data']/following::span[contains(@class,'oxd-checkbox-input')]")
))
consent_checkbox.click()

# Save Candidate
driver.find_element(By.XPATH, "//button[normalize-space()='Save']").click()

# --- Shortlist Candidate ---
# Wait for candidate row
candidate_row = wait.until(EC.presence_of_element_located((By.XPATH, "//div[contains(text(),'Omkar Test Candidate')]")))
candidate_row.click()

# Shortlist button
shortlist_btn = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[normalize-space()='Shortlist']")))
shortlist_btn.click()

# Confirm save shortlist
wait.until(EC.element_to_be_clickable((By.XPATH, "//button[normalize-space()='Save']"))).click()

# --- Schedule Interview ---
schedule_btn = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[normalize-space()='Schedule Interview']")))
schedule_btn.click()

wait.until(EC.presence_of_element_located((By.XPATH, "//label[text()='Interview Title']/following::input[1]"))).send_keys("Tech Interview")
driver.find_element(By.XPATH, "//label[text()='Interview Date']/following::input[1]").send_keys("2025-08-25")
driver.find_element(By.XPATH, "//label[text()='Interview Time']/following::input[1]").send_keys("10:30 AM")
driver.find_element(By.XPATH, "//label[text()='Interviewer']/following::input[1]").send_keys("Linda Anderson")

driver.find_element(By.XPATH, "//button[normalize-space()='Save']").click()

# --- Mark Candidate Pass ---
pass_btn = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[normalize-space()='Mark Passed']")))
pass_btn.click()
wait.until(EC.element_to_be_clickable((By.XPATH, "//button[normalize-space()='Save']"))).click()

# --- Hire Candidate ---
hire_btn = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[normalize-space()='Hire']")))
hire_btn.click()
wait.until(EC.element_to_be_clickable((By.XPATH, "//button[normalize-space()='Save']"))).click()

# --- Delete Candidate ---
driver.back()  # Go back to candidate list
time.sleep(3)

# Find and delete candidate
delete_icon = wait.until(EC.element_to_be_clickable((By.XPATH, "//div[contains(text(),'Omkar Test Candidate')]/ancestor::div[@role='row']//i[contains(@class,'bi-trash')]")))
delete_icon.click()

# Confirm delete
wait.until(EC.element_to_be_clickable((By.XPATH, "//button[normalize-space()='Yes, Delete']"))).click()

print("✅ Candidate workflow completed successfully!")

time.sleep(3)
driver.quit()

# ================== VACANCIES ==================
driver.find_element(By.XPATH, "//a[text()='Vacancies']").click()

# --- Add Vacancy ---
wait.until(EC.element_to_be_clickable((By.XPATH, "//button[text()='Add']"))).click()

# Vacancy Name
wait.until(EC.presence_of_element_located((By.XPATH, "//label[text()='Vacancy Name']/following::input"))).send_keys("Automation Test Engineer")

# Job Title dropdown
driver.find_element(By.XPATH, "//label[text()='Job Title']/following::div[1]").click()
time.sleep(1)
driver.find_element(By.XPATH, "//div[@role='listbox']//div[1]").click()

# Description
driver.find_element(By.XPATH, "//label[text()='Description']/following::textarea").send_keys("Automation role requiring Selenium + Python")

# Hiring Manager
driver.find_element(By.XPATH, "//label[text()='Hiring Manager']/following::input").send_keys("Linda Anderson")
time.sleep(2)
driver.find_element(By.XPATH, "//div[@role='listbox']//div[1]").click()

# No. of Positions
driver.find_element(By.XPATH, "//label[text()='No of Positions']/following::input").send_keys("2")

# Save Vacancy
driver.find_element(By.XPATH, "//button[text()='Save']").click()
time.sleep(2)

print("✅ Recruitment Module Automation Test Completed Successfully")

driver.quit()
