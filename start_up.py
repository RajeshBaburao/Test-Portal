from selenium import webdriver
chrome_driver=webdriver.Chrome(executable_path=r"C:\Users\BENU\Downloads\chromedriver")
admin_login="admin"
admin_password="Admin123#"
Portal_url=chrome_driver.get('https://ankitairen.github.io/')

#####Login Page####

Login_path="//*[@id='userid']"
Login_pass_path="//*[@id='password']"
Login_enter="/html/body/div/div/div[2]/form/button"
Add_user="/html/body/div/div/div[2]/form/button"


###### Add User Page#######

User_id="/html/body/div/div/div[2]/form/div[1]/input[1]"
User_Password="/html/body/div/div/div[2]/form/div[1]/input[2]"
User_name="firstname"
User_Lastname="lastname"

#### Add User ######

userid="id"
userpassword="password"
User_name="firstname"
User_Lastname="lastname"
Add_user_path="/html/body/div/div/div[2]/form/button"

#### User Credentials #####

user_first_id="user1"
user_First_name="first_user"
user_Last_name="first_user_lastname"
user_passs="User123#"



