from selenium import webdriver
import time


chrome_driver_path = r"C:\Drivers\chromedriver-win32\chromedriver.exe"
chrome_service = webdriver.ChromeService(chrome_driver_path)
driver = webdriver.Chrome(service=chrome_service)

# Navigate to the login page
driver.get("https://flamboyant-allen-00cf47.netlify.app/login")

# Negative TestCase:1 (Invalid email)
email_input = driver.find_element("name", "email")
email_input.send_keys("Suman5yopmail.com")
time.sleep(4)
email_input.clear()


# Negative TestCase:2 (Invalid email, Invalid password)
email_input = driver.find_element("name", "email")
email_input.send_keys("Suman5@yopmail.com")
password_input = driver.find_element("name", "password")
password_input.send_keys("Test123")
login_button = driver.find_element("xpath", "/html/body/app-root/app-login/div/div/div[1]/form/div[3]/app-button")
login_button.click()
time.sleep(5)
email_input.clear()
password_input.clear()

# Negative TestCase:3 (Valid email, Invalid password)
email_input = driver.find_element("name", "email")
email_input.send_keys("Suman51@yopmail.com")
password_input = driver.find_element("name", "password")
password_input.send_keys("Test123")
login_button = driver.find_element("xpath", "/html/body/app-root/app-login/div/div/div[1]/form/div[3]/app-button")
login_button.click()
time.sleep(5)
email_input.clear()
password_input.clear()

# Negative TestCase:4 (InValid email, valid password)
email_input = driver.find_element("name", "email")
email_input.send_keys("Suman1@yopmail.com")
password_input = driver.find_element("name", "password")
password_input.send_keys("Test@123")
login_button = driver.find_element("xpath", "/html/body/app-root/app-login/div/div/div[1]/form/div[3]/app-button")
login_button.click()
time.sleep(5)
email_input.clear()
password_input.clear()

# Positive TestCase (Valid email, valid password)
email_input = driver.find_element("name", "email")
password_input = driver.find_element("name", "password")
login_button = driver.find_element("xpath", "/html/body/app-root/app-login/div/div/div[1]/form/div[3]/app-button")


email_input.send_keys("Suman51@yopmail.com")
password_input.send_keys("Test@123")
login_button.click()

time.sleep(8)
driver.quit()
