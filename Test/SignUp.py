from selenium import webdriver
import time
from faker import Faker
faker = Faker()
fake_email = faker.email()


chrome_driver_path = r"C:\Drivers\chromedriver-win32\chromedriver.exe"
chrome_service = webdriver.ChromeService(chrome_driver_path)
driver = webdriver.Chrome(service=chrome_service)

# Navigate to the Signup page
driver.get("https://flamboyant-allen-00cf47.netlify.app/login")
signup_link = driver.find_element("xpath", "/html/body/app-root/app-login/div/div/div[1]/p/a")
signup_link.click()
time.sleep(5)

# Nagative TestCase : 1 (Invalid name)
name_input = driver.find_element("id", "name")
name_input.send_keys("Suman9")
time.sleep(2)
name_input.clear()

# Nagative TestCase :2 (Empty data )
next_button = driver.find_element("xpath", "/html/body/app-root/app-signup-page/app-signup/div/div/div[1]/form/div[6]/app-button/button")
next_button.click()
time.sleep(2)

# Positive TestCase (All Valid Data)
name_input = driver.find_element("id", "name")
name_input.send_keys("Suman")
radio_button = driver.find_element("xpath", "/html/body/app-root/app-signup-page/app-signup/div/div/div[1]/form/div[2]/mat-radio-group/mat-radio-button[1]")
radio_button.click()
dob_button = driver.find_element("xpath", "/html/body/app-root/app-signup-page/app-signup/div/div/div[1]/form/div[3]/mat-form-field/div/div[1]/div[2]/mat-datepicker-toggle/button/span[1]")
dob_button.click()
time.sleep(3)
day_button = driver.find_element("xpath", "/html/body/div[1]/div[2]/div/mat-datepicker-content/div[2]/mat-calendar/div/mat-month-view/table/tbody/tr[3]/td[5]/div[1]")
day_button.click()
time.sleep(5)
fake_mobile_number = "98" + str(faker.random_number(digits=8))
phone_input = driver.find_element("id", "phone")
phone_input.send_keys(fake_mobile_number)
time.sleep(3)
email_input = driver.find_element("id", "email")
email_input.send_keys(fake_email)
time.sleep(3)
next_button = driver.find_element("xpath", "/html/body/app-root/app-signup-page/app-signup/div/div/div[1]/form/div[6]/app-button/button")
next_button.click()
time.sleep(10)
password_input = driver.find_element("id", "password")
password_input.send_keys("Suman@1234")
confirm_input = driver.find_element("name", "confirmPassword")
confirm_input.send_keys("Suman@1234")
time.sleep(6)
signup_button = driver.find_element("xpath", "/html/body/app-root/app-signup-page/app-set-password/div/div/div[1]/form/div[3]/app-button/button")
signup_button.click()
time.sleep(6)
