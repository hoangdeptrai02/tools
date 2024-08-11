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

class TudongXoaNem :

    def __init__( self,imgP : str, dwlP : str ):
        self.image_path = imgP
        self.download_path = dwlP
        self.nameIMG = "2"
        self.isend = True

        # Tạo thư mục download nếu chưa tồn tại
        os.makedirs(self.download_path, exist_ok=True)
        self.conDrive()


    def conDrive(self):
     # Kết nối tới Chrome đang mở với remote debugging
        chrome_debugger_address = "127.0.0.1:9222"
        options = webdriver.ChromeOptions()
        options.add_experimental_option("debuggerAddress", chrome_debugger_address)

        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    
    async def send_keys_async(self,file_input, image_path):
        loop = asyncio.get_running_loop()
        await loop.run_in_executor(None, file_input.send_keys, image_path)

    async def batDauXoa(self):
        try:
            self.driver.get('https://app.photoroom.com/create')

            wait = WebDriverWait(self.driver, 10)
            file_input = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="root"]/div/div[2]/div[2]/div/div[1]/div/div/input')))
            #await file_input.send_keys(self.image_path)
            await self.send_keys_async(file_input,self.image_path)

            #await asyncio.sleep(5)  # Thay vì time.sleep

            btn_bg = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[4]/div/div[2]/div[1]/div/div[2]/div/div[2]/div/div[2]/div/span/div/button')))
            btn_bg.click()

            btn_rmBG = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[7]/div/div[5]')))
            btn_rmBG.click()

            await asyncio.sleep(2)  # Thay vì time.sleep

            intermediate_button = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="root"]/div/div[2]/div[1]/div/div[2]/div/div[3]/div/button[3]')))
            intermediate_button.click()

            download_button = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[4]/div/div[2]/div[1]/div/div[2]/div/div[3]/div/div/div/div/div/form/div[2]/button')))
            download_button.click()

            await asyncio.sleep(2)  # Thay vì time.sleep

        finally:
            self.isend = True

        print("Quá trình tự động hóa đã hoàn thành.")