from selenium import webdriver
from selenium import common
import time
username=input("Enter Username:")
password=input("Enter Password:")
baseurl=input("Enter Login page URL:")
course_no=input("Enter course no (as in the no of blue blocks in the home page)(if only one enter as one)")
level_url=input("Enter first question url(Varies from Level to Level):")#open the first question and in the level you want to download and paste that url here
browser = webdriver.Chrome()  
browser.get(baseurl)
#-------------
failed_list=open("Failed to download.txt",mode='w')
#-------------
time.sleep(2) 
unip = browser.find_element_by_xpath('/html/body/app-root/div/app-login/div/mat-card/div[2]/form/mat-form-field[1]/div/div[1]/div/input')
unip.send_keys(username)
pas = browser.find_element_by_xpath('/html/body/app-root/div/app-login/div/mat-card/div[2]/form/mat-form-field[2]/div/div[1]/div[1]/input')
pas.send_keys(password)
time.sleep(1)
login=browser.find_element_by_xpath('/html/body/app-root/div/app-login/div/mat-card/div[2]/form/button')
login.click()
time.sleep(5)
#---------------
homeredirect=browser.find_element_by_xpath('/html/body/app-root/div/app-student-home/div/mat-card/div/div['+course_no+']') 
homeredirect.click()
time.sleep(5)
browser.get(level_url)
time.sleep(5)
for i in range(1,100):
    evala=browser.find_element_by_xpath('/html/body/app-root/div/app-student-solve/div[2]/app-solve-question/div/div/div[2]/mat-card/div[3]/button[2]')
    evala.click()
    time.sleep(3)
    try:
        down=browser.find_element_by_xpath('/html/body/app-root/div/app-student-solve/div[2]/app-solve-question/div/div/div[2]/mat-card/div[4]/a[2]')
        down.click()
    except:
        failed_list.write("Unable to download Q"+str(i)+"\n")
    time.sleep(1)
    nextb=browser.find_element_by_xpath('/html/body/app-root/div/app-student-solve/div[1]/button[2]')
    nextb.click()
    time.sleep(2)
evala=browser.find_element_by_xpath('/html/body/app-root/div/app-student-solve/div[2]/app-solve-question/div/div/div[2]/mat-card/div[3]/button[2]')
evala.click()
time.sleep(3)
try:
    down=browser.find_element_by_xpath('/html/body/app-root/div/app-student-solve/div[2]/app-solve-question/div/div/div[2]/mat-card/div[4]/a[2]')
    down.click()
except:
    failed_list.write("Unable to download Q100")
browser.quit()

