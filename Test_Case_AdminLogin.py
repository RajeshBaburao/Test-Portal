'''
Test-Case Objective: Verify Access to User-Portal with proper login credentials(by using admin credentials).
'''
from selenium import webdriver
import time
import start_up
config=start_up

driver=config.chrome_driver   ##Using Driver Path
config.Portal_url             ##Accessing the Portal URL
driver.implicitly_wait(10)

ele=driver.find_element_by_xpath(config.Login_path)        ## Verifying Login Path & entering the credentials
if ele.is_displayed():
    ele.send_keys(config.admin_login)
    print("Entered logged in correct")

ele_pass=driver.find_element_by_xpath(config.Login_pass_path)   ## Verifying Path for password & entering the credentials
if ele_pass.is_displayed():
    ele_pass.send_keys(config.admin_password)
    print("Password entered correct")

login=driver.find_element_by_xpath(config.Login_enter)
login.click()

driver.implicitly_wait(5)

ele_displayed=driver.find_element_by_xpath(config.Add_user)      ## Verifying the Parameters of next Page, after login
if ele_displayed.is_displayed():
    print("Logged in Successfully, expected parameters displayed")
else:
    print("could not successfully login")

user_id_enabled=driver.find_element_by_xpath(config.User_id)     ## Verifying User-ID Icon Enabled
if user_id_enabled.is_enabled():
    print("user-id icon is enabled")
else:
    print("user-id icon is not enabled")

user_pass=driver.find_element_by_xpath(config.User_Password)     ## Verifying User-Password Icon Enabled
if user_pass.is_enabled():
    print("user-password icon is enabled")
else:
    print("user-password icon is not enabled")

user_firstname=driver.find_element_by_name(config.User_name)     ## Verifying User-name Icon Enabled
if user_firstname.is_enabled():
    print("user-firstname icon is enabled")
else:
    print("user-firstname icon is not enabled")

user_lastname=driver.find_element_by_name(config.User_Lastname)    ## Verifying User-Lstname Icon Enabled
if user_lastname.is_enabled():
    print("user-lastname icon is enabled")
else:
    print("user-lastname icon is not enabled")


driver.quit()

