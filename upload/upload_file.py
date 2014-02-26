#-*-coding:utf-8-*-
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
import os

dr=webdriver.Chrome()
file_path='file:///'+os.path.abspath('upload_file.html')
dr.get(file_path)


dr.find_element_by_name('file').send_keys('C:\Users\acer\Desktop\webmobile\program\upload\upload_file.md')

sleep(2)
dr.quit()