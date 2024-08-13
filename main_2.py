from TudongXoaNem  import TudongXoaNem  
from ktrFolder import ktrFolder
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
import asyncio

image_path = r'C:\Users\PC\Desktop\tool\2.png'
download_path = r'G:\My Drive\23.Hoàng\rmb_save_here'
#folderImg_path = input("Paste thư mục chứa ảnh vào đây: ")
folderImg_path = r'C:\Users\PC\Desktop\tool\Chua_hinh'
atRmBg = TudongXoaNem(image_path,download_path) # ham init tudongxoanen

ktrFold = ktrFolder(folderImg_path)# ham init ktr foler

ktrFold.ktrFol() # lay anh trong folder

    
async def xuly():
    global image_path
    isWait = False
    while True:
        if( len(ktrFold.imgs) <=0 ): 
            if(isWait == False):
                print("dang cho anh")
                print("so luong anh dang co: " + str(len(ktrFold.imgs)))
                isWait = True

            ktrFold.ktrFol() # lay anh trong folder
            await asyncio.sleep(1)
            continue
        print("\nso luong anh dang co: " + str(len(ktrFold.imgs)))
        isWait = False
        atRmBg.isend = False
        image_path = ktrFold.getPathImg()
        atRmBg.image_path = image_path

        await atRmBg.batDauXoa()
        if(atRmBg.isend) :
            ktrFold.rmImg(image_path)
        


asyncio.run(xuly())

