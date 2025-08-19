from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd
import time

# -----------------------
# Setup Chrome driver
# -----------------------
driver = webdriver.Chrome()  # Ensure chromedriver is in PATH
driver.maximize_window()

# Base URL
base_url = "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"

# -----------------------
# Load login test cases from "login" sheet
# -----------------------
df = pd.read_excel(
    r"C:\Users\Omkar\Documents\GitHub\OrangeHRM-manual-tesing\Test Cases OrangeHRM.xlsx",
    sheet_name="login",
    header=1  # first row is header
)
df.columns = df.columns.str.strip()  # Strip spaces from column names

# -----------------------
# Loop through each test case
# -----------------------
for index, row in df.iterrows():
    test_id = row['TestCaseId']
    test_data = str(row['Test Data']).strip() if not pd.isna(row['Test Data']) else ""
    expected_result = str(row['Expected Result']).strip() if not pd.isna(row['Expected Result']) else ""

    print(f"\nRunning {test_id} ...")

    # Open login page
    driver.get(base_url)
    time.sleep(1)  # small wait for page load

    # Wait for username field
    username_field = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.NAME, "username"))
    )
    password_field = driver.find_element(By.NAME, "password")

    # -----------------------
    # Determine credentials
    # -----------------------
    if test_id == "TC_LOGIN_001":
        username = "Admin"
        password = "admin123"
    else:
        username = ""
        password = ""
        if "Username:" in test_data:
            try:
                username = test_data.split("Username:")[1].split()[0].strip()
            except:
                pass
        if "Passowrd:" in test_data:
            try:
                password = test_data.split("Passowrd:")[1].strip()
            except:
                pass

    # -----------------------
    # Enter credentials
    # -----------------------
    if username:
        username_field.clear()
        username_field.send_keys(username)
    if password:
        password_field.clear()
        password_field.send_keys(password)

    # Click login button (only if credentials exist)
    if username or password:
        driver.find_element(By.XPATH, "//button[@type='submit']").click()
        time.sleep(2)

    # -----------------------
    # Verification & special cases
    # -----------------------
    try:
        # -----------------------
        # Successful login (TC_LOGIN_001)
        # -----------------------
        if test_id == "TC_LOGIN_001":
            dashboard_header = WebDriverWait(driver, 10).until(
                EC.visibility_of_element_located((By.XPATH, "//h6[text()='Dashboard']"))
            )
            assert dashboard_header.is_displayed()
            print(f"{test_id} passed! Dashboard loaded successfully.")

            # Logout to reset for next test
            driver.find_element(By.XPATH, "//p[@class='oxd-userdropdown-name']").click()
            time.sleep(1)
            driver.find_element(By.LINK_TEXT, "Logout").click()
            time.sleep(2)

        # -----------------------
        # Invalid credentials
        # -----------------------
        elif "Invalid credentials" in expected_result:
            error = WebDriverWait(driver, 5).until(
                EC.visibility_of_element_located((By.XPATH, "//p[contains(@class,'oxd-alert-content-text')]"))
            ).text
            assert "Invalid credentials" in error
            print(f"{test_id} passed! Invalid credentials error shown.")

        # -----------------------
        # Required field warnings
        # -----------------------
        elif "Required field warnings" in expected_result:
            warnings = driver.find_elements(By.XPATH, "//span[contains(@class,'oxd-input-field-error')]")
            assert len(warnings) > 0
            print(f"{test_id} passed! Required field warnings shown.")

        # -----------------------
        # Password masking
        # -----------------------
        elif "Password characters should be masked" in expected_result:
            assert password_field.get_attribute("type") == "password"
            print(f"{test_id} passed! Password masked correctly.")

        # -----------------------
        # Login button enabled state
        # -----------------------
        elif "Login button remains enabled" in expected_result:
            login_btn = driver.find_element(By.XPATH, "//button[@type='submit']")
            assert login_btn.is_enabled()
            print(f"{test_id} passed! Login button state verified.")

        # -----------------------
        # Remember me (optional)
        # -----------------------
        elif test_id == "TC_LOGIN_006":
            try:
                remember_me = driver.find_elements(By.XPATH, "//input[@type='checkbox']")
                if len(remember_me) > 0:
                    print(f"{test_id}: 'Remember me' option is present.")
                else:
                    print(f"{test_id}: 'Remember me' option NOT present (expected).")
            except Exception:
                print(f"{test_id}: 'Remember me' option NOT present (expected).")

        # -----------------------
        # Page responsiveness (optional)
        # -----------------------
        elif test_id == "TC_LOGIN_007":
            try:
                driver.set_window_size(400, 800)  # mobile
                time.sleep(1)
                driver.set_window_size(1200, 800)  # desktop
                print(f"{test_id}: Page responsiveness checked (manual verification may be needed).")
            except Exception:
                print(f"{test_id}: Page responsiveness check skipped.")

        # -----------------------
        # Forgot password cases
        # -----------------------
        elif test_id in ["TC_LOGIN_008", "TC_LOGIN_009", "TC_LOGIN_010"]:
            # Navigate to login page again
            driver.get(base_url)
            WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.NAME, "username"))
            )

            # Click forgot password link reliably
            try:
                # Scroll the link into view and click
                forgot_password = WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located((By.LINK_TEXT, "Forgot your password?"))
                )
                driver.execute_script("arguments[0].scrollIntoView(true);", forgot_password)
                time.sleep(0.5)
                forgot_password.click()

                forgot_password.click()

                time.sleep(1)
            except Exception:
                print(f"{test_id}: Forgot Password link not found!")
                continue

            if test_id == "TC_LOGIN_008":
                assert "requestPasswordResetCode" in driver.current_url
                print(f"{test_id} passed! Reset password page displayed.")

            elif test_id == "TC_LOGIN_009":
                driver.find_element(By.NAME, "username").send_keys("Admin")
                driver.find_element(By.XPATH, "//button[@type='submit']").click()
                time.sleep(1)
                msg = driver.find_element(By.XPATH, "//p[contains(@class,'oxd-text--toast-message')]").text
                assert "success" in msg.lower()
                print(f"{test_id} passed! Password reset for valid username.")

            elif test_id == "TC_LOGIN_010":
                driver.find_element(By.NAME, "username").send_keys("Wrongusername")
                driver.find_element(By.XPATH, "//button[@type='submit']").click()
                time.sleep(1)
                msg = driver.find_element(By.XPATH, "//p[contains(@class,'oxd-text--toast-message')]").text
                assert "not found" in msg.lower() or "error" in msg.lower()
                print(f"{test_id} passed! Error shown for invalid username.")

        # -----------------------
        # Fallback
        # -----------------------
        else:
            print(f"{test_id} skipped verification (no matching condition).")

    except Exception as e:
        print(f"{test_id} failed! Error: {e}")

# Close browser
driver.quit()
print("\nAll login tests completed.")
