#!/usr/bin/python
import os
import glob
import fnmatch
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException

os.chdir("./JPEGS")

# Login Page-----------------------------------------------
userName = "noelt"
passWord = "N51663T"
# hlNumber = os.environ["item"]
# hlNumber = raw_input("What's the HL Item with leading zeros #: ")
hlNumber = ("00277252")
driver = webdriver.Chrome("/usr/local/bin/chromedriver")
driver.get("http://hl-intranet/CloserLook/start.asp");

inputElement = driver.find_element_by_id("userid").send_keys(userName)
inputElement = driver.find_element_by_id("password").send_keys(passWord)
driver.find_element_by_class_name("button").click()

# NEW - Create a NEW closer look
driver.find_element_by_partial_link_text('New Closer Look').click()
inputElement = driver.find_element_by_name('clID').send_keys(hlNumber)
driver.find_element_by_name('Submit').click()

# EXPERIMENTAL - IF CL exists


try:
    theAlert = driver.find_element_by_xpath("/html/body/table[2]/tbody/tr/td[2]/form/table/tbody/tr[1]/td")
    print("This CL already exists!")
    driver.back()
    driver.back()
    driver.find_element_by_name('itemNumber').send_keys(hlNumber)
    driver.find_element_by_name('Submit').click()
    driver.find_element_by_partial_link_text('Imag').click()
except NoSuchElementException:
        print ("No wait this is a NEW CL!")
        driver.find_element_by_partial_link_text('Imag').click()

try:
    driver.find_element_by_name('deleteAll').click()
    alert = driver.switch_to_alert()
    alert.accept()
except NoSuchElementException:
    pass
    # driver.find_element_by_name('itemNumber').send_keys(hlNumber)
    # driver.find_element_by_name('Submit').click()

# Define FC
full_FC = hlNumber + "_Cover.jpg"
full_FCt = hlNumber + "_Covert.jpg"
full_FCz = hlNumber + "_Coverz.jpg"
# Define BC
full_BC = hlNumber + "_BCover.jpg"
full_BCt = hlNumber + "_BCovert.jpg"
full_BCz = hlNumber + "_BCoverz.jpg"

# Front Cover--------------------------------------------
driver.find_element_by_name('caption').send_keys("Front Cover")
driver.find_element_by_name("fullImage").send_keys(os.getcwd()+"/"+full_FC)
driver.find_element_by_name("thumbnailImage").send_keys(os.getcwd()+"/"+full_FCt)
driver.find_element_by_name("zoomImage").send_keys(os.getcwd()+"/"+full_FCz)
driver.find_element_by_name('save').click()

# print realFileCount
realFileCount = len(fnmatch.filter(os.listdir('.'), '*.jpg'))
realFileCount = realFileCount - 6
counter = 0
num = 1

while counter < realFileCount:
    captionNumber = 1
    caption = ("Sample Page " + str(num))
    full_Page = hlNumber + "_Page-"+str(num)+".jpg"
    full_Paget = hlNumber + "_Page-"+str(num)+"t.jpg"
    full_Pagez = hlNumber + "_Page-"+str(num)+"z.jpg"
    driver.find_element_by_name('caption').send_keys(caption)
    driver.find_element_by_name("fullImage").send_keys(os.getcwd()+"/"+full_Page)
    driver.find_element_by_name("thumbnailImage").send_keys(os.getcwd()+"/"+full_Paget)
    driver.find_element_by_name("zoomImage").send_keys(os.getcwd()+"/"+full_Pagez)
    driver.find_element_by_name('save').click()
    counter = counter + 3
    num = num + 1

# Back Cover--------------------------------------------
driver.find_element_by_name('caption').send_keys("Back Cover")
driver.find_element_by_name("fullImage").send_keys(os.getcwd()+"/"+full_BC)
driver.find_element_by_name("thumbnailImage").send_keys(os.getcwd()+"/"+full_BCt)
driver.find_element_by_name("zoomImage").send_keys(os.getcwd()+"/"+full_BCz)
driver.find_element_by_name('save').click()