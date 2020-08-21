'''
Test-Case Objective:
Scenario-1Verify Users are successfully able to add & displayed in the table entry.
Scenario-2:Verify after logging out from the portal & re-logging in, new added users are still be visible under table entry.
Scenario-3:Verify logging from newly added user credentials.
Scenario-4:Verify Modifying the parameters for existing user.
'''
from selenium import webdriver
import time
import start_up
import Login
config=start_up

Login.Admin_Login()           ## Logging in as Admin
driver=config.chrome_driver   ##Using Driver Path

class Add_User_cred():

    def AddUser(self):
	
        self.user_id_enabled=driver.find_element_by_name(config.userid)     ## Verifying User-ID Icon Enabled & enter the Keys
        if self.user_id_enabled.is_enabled():
            print("user-id icon is enabled")
            self.user_id_enabled.send_keys(config.user_first_id)
        else:
            print("user-id icon is not enabled")

        self.user_pass=driver.find_element_by_name(config.userpassword)     ## Verifying User-Password Icon Enabled & enter the Keys
        if self.user_pass.is_enabled():
            print("user-password icon is enabled")
            self.user_pass.send_keys(config.user_passs)
        else:
            print("user-password icon is not enabled")

        self.user_firstname=driver.find_element_by_name(config.User_name)     ## Verifying User-name Icon Enabled & enter the Keys
        if self.user_firstname.is_enabled():
            print("user-firstname icon is enabled")
            self.user_firstname.send_keys(config.user_First_name)
        else:
            print("user-firstname icon is not enabled")

        self.user_lastname=driver.find_element_by_name(config.User_Lastname)    ## Verifying User-Lstname Icon Enabled & enter the Keys
        if self.user_lastname.is_enabled():
            print("user-lastname icon is enabled")
            self.user_lastname.send_keys(config.user_Last_name)
        else:
            print("user-lastname icon is not enabled")

        ele_displayed=driver.find_element_by_xpath(config.Add_user_path)  ## click add user
        ele_displayed.click()

        driver.implicitly_wait(5)

        self.user_name=driver.find_element_by_xpath("//*[@id='userTable']/tbody/tr[2]/td[1]").text
        self.user_first_name=driver.find_element_by_xpath("//*[@id='userTable']/tbody/tr[2]/td[2]").text
        self.user_last_name=driver.find_element_by_xpath("//*[@id='userTable']/tbody/tr[2]/td[3]").text
        self.user_password=driver.find_element_by_xpath("//*[@id='userTable']/tbody/tr[2]/td[4]").text

    def Verify_user(self):																				###Verify New added Users in the Table Entry
        if self.user_name==config.user_first_id:
            print("Username is present in table entry")
        else:
            print("username is not present")

        if self.user_first_name==config.user_First_name:
            print("firstname is present in table entry")
        else:
            print("firstname is not present in table entry")

        if self.user_last_name==config.user_Last_name:
            print("Lastname is present in table entry")
        else:
            print("Lastname is not present in table entry")

        if self.user_password==config.user_passs:
            print("User password is present in table entry")
        else:
            print("user password is not present in table entry")

    def Logout_Portal(self):																		#### Function to Log Out
        Logout=driver.find_element_by_xpath("/html/body/div/div/div[1]/nav/span[3]/a")
        Logout.click()

    def View_user(self):
        view_user=driver.find_element_by_xpath("/html/body/div/div/div[1]/nav/span[2]/a")			#### Function to check view users, from Admin Portal
        view_user.click()

    def Logging_with_new_added_credentials(self):
        ele=driver.find_element_by_xpath(config.Login_path)        ## Verifying Login Path & entering the credentials
        if ele.is_displayed():
            ele.send_keys(config.user_first_id)
            print("Entered logged in correct")

        ele_pass=driver.find_element_by_xpath(config.Login_pass_path)
        if ele_pass.is_displayed():
            ele_pass.send_keys(config.user_passs)
            print("Password entered correct")

        login=driver.find_element_by_xpath(config.Login_enter)
        login.click()

    def Update_user(self):                                                                   #### Updating the user credentials

        self.user_id_enabled=driver.find_element_by_xpath("/html/body/div/div/div[2]/form/div[1]/input[1]")     ## Verifying User-ID Icon Enabled & enter the Keys
        if self.user_id_enabled.is_enabled():
            print("user-id icon should not be enabled")
        else:
            print("user-id icon is not enabled as expected")

        self.user_firstname=driver.find_element_by_name(config.User_name)     ## Verifying User-name Icon Enabled & enter the Keys
        self.user_firstname.clear()
        if self.user_firstname.is_enabled():
            print("user-firstname icon is enabled")
            self.user_firstname.send_keys("first_user_new")                                     #### Change the firstname & observe, updates are populated on the page
        else:
            print("user-firstname icon is not enabled")

        user_update=driver.find_element_by_xpath("/html/body/div/div/div[2]/form/button")
        user_update.click()
        driver.implicitly_wait(10)
        updated_element=driver.find_element_by_xpath("/html/body/div/div/div[2]/form/div[3]/div[4]")
        if updated_element=="first_user_new":
            print("updated successfully")
        else:
            print("Modifications not populated on portal")

			
########
####Scenario-1Verify Users are successfully able to add & displayed in the table entry.
########			
			
user_verify_credentials=Add_User_cred()
user_verify_credentials.AddUser()
user_verify_credentials.Verify_user()
user_verify_credentials.Logout_Portal()

######
####Scenario-2:Verify after logging out from the portal & re-logging in, new added users are still be visible under table entry.
#######

Login.Admin_Login()
user_verify_credentials.View_user()
user_verify_credentials.Verify_user()
user_verify_credentials.Logout_Portal()

#########
######Scenario-3:Verify logging from newly added user credentials.
#########

user_verify_credentials.Logging_with_new_added_credentials()

#########
#####Scenario-4:Verify Modifying the parameters for existing user.
#########

user_verify_credentials.Update_user()

driver.quit()