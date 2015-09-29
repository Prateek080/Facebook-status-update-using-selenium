import urllib2,urllib, cookielib, re, os, sys

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import getpass
from selenium import webdriver
import time
import sys
from bs4 import BeautifulSoup


class Facebook:

    def login(self,email,password,status):
            '''
            function name : login
            function description: It accepts the email and password and status of the user and post it to Facebook
            :param email:
            :param password:
            :param status:
            :return:
            '''
            
            driver = webdriver.Firefox()
            driver.get("https://facebook.com")
              

            login="loginbutton"
            emailelement = driver.find_element_by_name("email")
            passwordelement = driver.find_element_by_name("pass")
            emailelement.send_keys(email)
            passwordelement.send_keys(password)
            loginelement = driver.find_element_by_id(login)

            #logging in to the facebook using Selenium
            loginelement.click()
            
            time.sleep(5)
            url=driver.current_url
            if(url=="https://www.facebook.com/login.php?login_attempt=1&lwv=110"):
                
                        print "Login failed"
                        driver.close()

            else:
                        BeautifulSoup(driver.page_source)

                        
                        #posting to the facebook
                        statuselement = driver.find_element_by_id("u_0_12")
                        statuselement.send_keys(status)
                        statuselement = driver.find_elements_by_class_name("_4jy1")
                        statuselement[0].click()
                        print "Status Updated"

                       

                        driver.close()

                        
                        

                        


    def inp(self):
            '''
            function name : login
            function description : It accepts the username and password and status from the terminal and sends
                                    the login function
            :return:
            '''
            email=raw_input("Email Id: ")
            #input the password
            password=getpass.getpass("Password: ")
            #if the password is empty then it will ask for one more time.
            if password=="":
                password=getpass.getpass("Password is Blank.ReEnter Password: ")

            status=raw_input("Enter your status: ")
            call_2 = Facebook()
            call_2.login(email,password,status)
            

if __name__ == '__main__':         
            start = Facebook()
            start.inp()







