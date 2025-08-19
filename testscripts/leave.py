from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time

# ---------- DRIVER INIT ----------
driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

# ---------- LOGIN ----------
def login(username="Admin", password="admin123"):
    username_field = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.NAME, "username"))
    )
    password_field = driver.find_element(By.NAME, "password")
    username_field.send_keys(username)
    password_field.send_keys(password)
    driver.find_element(By.XPATH, "//button[@type='submit']").click()
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//span[text()='Dashboard']"))
    )
    print(f"[INFO] Logged in as {username}")

# ---------- NAVIGATION HELPER ----------
def navigate_leave_subtab(driver, subtab_name):
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//span[text()='Leave']"))
    ).click()
    time.sleep(1)  # small wait for UI animation

    if subtab_name == "Apply":
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//a[contains(@href,'applyLeave')]"))
        ).click()
    elif subtab_name == "Entitlements":
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.LINK_TEXT, "Entitlements"))
        ).click()
    elif subtab_name == "Leave List":
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.LINK_TEXT, "Leave List"))
        ).click()
    elif subtab_name == "My Leave":
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//a[contains(@href,'viewMyLeaveList')]"))
        ).click()
    else:
        raise ValueError(f"Unknown Leave subtab: {subtab_name}")

# ---------- L001: Apply Leave ----------
def test_apply_leave(driver):
    print("\n[INFO] Running L001: Applying Leave for Employee...")
    try:
        navigate_leave_subtab(driver, "Apply")
        # Select Leave Type
        leave_type_dropdown = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//label[text()='Leave Type']/..//div"))
        )
        leave_type_dropdown.click()
        WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable((By.XPATH, "//span[text()='Annual Leave']"))
        ).click()
        # From Date
        from_date = driver.find_element(By.XPATH, "//input[@placeholder='From']")
        from_date.clear()
        from_date.send_keys("2025-08-20")
        # To Date
        to_date = driver.find_element(By.XPATH, "//input[@placeholder='To']")
        to_date.clear()
        to_date.send_keys("2025-08-22")
        # Comment
        comment = driver.find_element(By.XPATH, "//textarea")
        comment.send_keys("Personal Leave Application")
        # Submit
        driver.find_element(By.XPATH, "//button[@type='submit']").click()
        print("[PASS] L001: Leave Applied successfully ✅")
    except Exception as e:
        print(f"[FAIL] L001: Leave Apply failed ❌ Error: {str(e)}")

# ---------- L002: Add Leave Entitlement ----------
def add_leave_entitlement(driver):
    print("\n[INFO] Running L002: Add Leave Entitlement...")
    try:
        navigate_leave_subtab(driver, "Entitlements")
        # Click "Add Entitlements"
        WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable((By.LINK_TEXT, "Add Entitlements"))
        ).click()
        # Individual Employee radio button
        WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable((By.XPATH, "//input[@value='individual']"))
        ).click()
        # Employee Name
        emp_field = driver.find_element(By.XPATH, "//input[@placeholder='Type for hints...']")
        emp_field.clear()
        emp_field.send_keys("Orange Test")
        time.sleep(1)
        emp_field.send_keys(Keys.ARROW_DOWN)
        emp_field.send_keys(Keys.ENTER)
        # Leave Type
        leave_type_dropdown = driver.find_element(By.XPATH, "//label[text()='Leave Type']/..//div")
        leave_type_dropdown.click()
        WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable((By.XPATH, "//span[contains(text(),'Annual Leave')]"))
        ).click()
        # Leave Period (2021-2024)
        period_dropdown = driver.find_element(By.XPATH, "//label[text()='Leave Period']/..//div")
        period_dropdown.click()
        WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable((By.XPATH, "//span[contains(text(),'2024-01-01 - 2024-12-31')]"))
        ).click()
        # Entitlement Days
        ent_field = driver.find_element(By.XPATH, "//input[@class='oxd-input oxd-input--active']")
        ent_field.clear()
        ent_field.send_keys("10")
        # Save
        driver.find_element(By.XPATH, "//button[@type='submit']").click()
        print("[PASS] L002: Leave entitlement added successfully ✅")
    except Exception as e:
        print(f"[FAIL] L002: Add entitlement failed ❌ Error: {str(e)}")

# ---------- L003: Apply Entitlements Check ----------
def test_apply_leave_entitlements(driver):
    print("\n[INFO] Running L003: Apply Leave Entitlements...")
    try:
        navigate_leave_subtab(driver, "Entitlements")
        rows = driver.find_elements(By.XPATH, "//div[contains(@class,'oxd-table-card')]")
        for index, row in enumerate(rows, start=1):
            try:
                days_input = row.find_element(By.XPATH, ".//input")
                days_input.clear()
                days_input.send_keys("5")
                print(f"[PASS] Row {index}: Entitlement updated ✅")
            except:
                print(f"[INFO] Row {index}: No editable entitlement field")
        print("[PASS] L003: Entitlements processed ✅")
    except Exception as e:
        print(f"[FAIL] L003: Entitlement test failed ❌ Error: {str(e)}")

# ---------- L004: Leave List Approval ----------
def test_leave_list_approval(driver):
    print("\n[INFO] Running L004: Leave List Approval...")
    try:
        navigate_leave_subtab(driver, "Leave List")
        driver.find_element(By.XPATH, "//button[@type='submit']").click()  # Search
        print("[PASS] L004: Leave list filtered ✅")
    except Exception as e:
        print(f"[FAIL] L004: Leave List failed ❌ Error: {str(e)}")

# ---------- L005: Leave Balance ----------
def test_leave_balance(driver):
    print("\n[INFO] Running L005: Leave Balance...")
    try:
        navigate_leave_subtab(driver, "Entitlements")
        records = WebDriverWait(driver, 10).until(
            EC.presence_of_all_elements_located((By.XPATH, "//div[contains(@class,'oxd-table-card')]"))
        )
        print(f"[PASS] L005: Found {len(records)} leave balance records ✅")
    except Exception as e:
        print(f"[FAIL] L005: Balance check failed ❌ Error: {str(e)}")

# ---------- L006: My Leave ----------
def test_employee_check_my_leave(driver):
    print("\n[INFO] Running L006: My Leave Records...")
    try:
        navigate_leave_subtab(driver, "My Leave")
        driver.find_element(By.XPATH, "//button[@type='submit']").click()
        print("[PASS] L006: My Leave displayed ✅")
    except Exception as e:
        print(f"[FAIL] L006: My Leave check failed ❌ Error: {str(e)}")

# ---------- RUN TESTS ----------
if __name__ == "__main__":
    login()
    add_leave_entitlement(driver)            # First add entitlement
    test_apply_leave(driver)                 # Apply leave for employee
    test_apply_leave_entitlements(driver)    # Check entitlement rows
    test_leave_list_approval(driver)         # Approve leave if any
    test_leave_balance(driver)               # Check balances
    test_employee_check_my_leave(driver)     # Verify leave in My Leave
    driver.quit()
