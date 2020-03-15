#coding=utf-8
import configparser
class ReadIni(object):
    def __init__(self):
       # self.cf = self.load_ini()
       self.cf= configparser.ConfigParser()
       self.cf.read(r"C:\pythoncode\config\LocalElement.ini")
       



    def get_value(self,value):  
        data= self.cf.get('RegisterElement',value)
        by=data.split('>')[0]
        element=data.split('>')[1]
        return data

if __name__ == "__main__":
    init= ReadIni()
    print(init.get_value('user_email'))
