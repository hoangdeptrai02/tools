from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import time
import os
import glob
import asyncio
img_extensions = ('*.jpg', '*.jpeg', '*.png')
class ktrFolder:

    def __init__(self,folder_path):
        self.folder_path = folder_path
        self.imgs = []

    def ktrFol(self):
        for ex in img_extensions:
            self.imgs.extend(glob.glob(os.path.join(self.folder_path,ex)))
        

    def getPathImg(self):
        print("lay path anh")
        return self.imgs[0]
    
    def rmImg(self,img):
        try:
            os.remove(img)
            self.imgs.remove(img)
        except:
            print("ERROR!!!_: CAN NOT REMOVE IMG")


        

