from selenium import webdriver
import time

dr=webdriver.Chrome()
time.sleep(2)
print 'maximize brower' 

dr.maximize_window()

time.sleep(2)
print 'close brower'

dr.quit()
