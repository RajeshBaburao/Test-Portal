import time
import start_up
config=start_up

def Admin_Login():

    driver=config.chrome_driver   ##Using Driver Path
    config.Portal_url             ##Accessing the Portal URL
    driver.implicitly_wait(10)

    ele=driver.find_element_by_xpath(config.Login_path)        ## Verifying Login Path & entering the credentials
    if ele.is_displayed():
        ele.send_keys(config.admin_login)
        print("Entered logged in correct")

    ele_pass=driver.find_element_by_xpath(config.Login_pass_path)
    if ele_pass.is_displayed():
        ele_pass.send_keys(config.admin_password)
        print("Password entered correct")

    login=driver.find_element_by_xpath(config.Login_enter)
    login.click()

    #driver.implicitly_wait(5)