from selenium import webdriver
import time


chrome_driver_path = r"C:\Drivers\chromedriver-win32\chromedriver.exe"
chrome_service = webdriver.ChromeService(chrome_driver_path)
driver = webdriver.Chrome(service=chrome_service)

# Navigate to the Signup page
driver.get("https://flamboyant-allen-00cf47.netlify.app/login")
time.sleep(2)
signup_link = driver.find_element("xpath", "/html/body/app-root/app-login/div/div/div[1]/form/div[2]/div[1]/a")
signup_link.click()
time.sleep(5)

# Nagative Testcase: 1 ( invalid email)
email_input = driver.find_element("id", "email")
email_input.send_keys("Suman5yopmail.com")
time.sleep(4)
email_input.clear()

# Nagative Testcase: 2 (unregistered email)
email_input = driver.find_element("id", "email")
email_input.send_keys("Suman5@yopmail.com")
send_button = driver.find_element("xpath", "/html/body/app-root/app-forgot-password/div/div/div[1]/form/div[2]/app-button")
send_button.click()
time.sleep(4)
email_input.clear()

# Positive Testcase: 2 (registered email)
email_input = driver.find_element("id", "email")
email_input.send_keys("Suman51@yopmail.com")
send_button = driver.find_element("xpath", "/html/body/app-root/app-forgot-password/div/div/div[1]/form/div[2]/app-button")
send_button.click()
time.sleep(4)
driver.quit()

