#coding=utf-8
import sys
sys.path.append ('C:\pythoncode')
from util.read_ini import ReadIni
from selenium import webdriver
import time
class FoundElement ():
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.get("http://www.5itest.cn/register")
        self.init= ReadIni()
        time.sleep(5)

    def getElement(self,value):

        data=self.init.get_value(value)
        by=data.split('>')[0]
        element=data.split('>')[1]
        if by=='id':
            self.driver.find_element_by_id(element).send_keys('111')

    def close(self):
        self.driver.close()        

if __name__ == "__main__":
    element= FoundElement()
    element.getElement('user_email')        
    time.sleep(5)
    element.close()



     