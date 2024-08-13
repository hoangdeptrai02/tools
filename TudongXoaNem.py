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
import json
from selenium.webdriver.common.alert import Alert
from selenium.common.exceptions import NoAlertPresentException
from selenium.common.exceptions import WebDriverException

# Khởi tạo driver với tùy chọn DevTools Protocol
caps = DesiredCapabilities.CHROME
caps['goog:loggingPrefs'] = {'performance': 'ALL'}
class TudongXoaNem :

    def __init__( self,imgP : str, dwlP : str ):
        self.image_path = imgP
        self.download_path = dwlP
        self.nameIMG = "2"
        self.isend = True
        self.isOpen = False
        # Tạo thư mục download nếu chưa tồn tại
        os.makedirs(self.download_path, exist_ok=True)
        self.conDrive()


    def conDrive(self):
     # Đường dẫn đến thư mục profile Chrome của bạn
        profile_path = r'C:\ChromeProfiles'
        
        options = webdriver.ChromeOptions()

        prefs = {"profile.default_content_setting_values.notifications": 2}  # Vô hiệu hóa thông báo
        options.add_experimental_option("prefs", prefs)

        # Chỉ định thư mục profile
        options.add_argument(f"user-data-dir={profile_path}")
        options.add_argument("profile-directory=Profile_13")
        #options.add_argument("--headless=new")
        #options.add_argument("--disable-gpu")  # Có thể cần thiết cho một số hệ điều hành 
        options.add_argument("--window-size=1920,1080")  # Chỉ định kích thước cửa sổ
        #options.add_argument("--no-sandbox")  # Cô lập hoàn toàn phiên làm việc
        #options.add_argument("--remote-debugging-port=9222")  # Thêm tùy chọn này
        #options.add_argument("--disable-dev-shm-usage")  # Thêm tùy chọn này
        #options.add_argument("--disable-extensions")
        #options.add_argument("--disable-infobars")
        #options.add_argument("--disable-notifications")
    
        # Lấy các log từ DevTools
        self.logs = self.driver.get_log('performance')
        
        self.driver.get('https://app.photoroom.com/create')
    
    async def send_keys_async(self,file_input, image_path):
        loop = asyncio.get_running_loop()
        await loop.run_in_executor(None, file_input.send_keys, image_path)

    def isAlert(self):
        try:
            # Kiểm tra sự hiện diện của cảnh báo
            self.alert = self.driver.switch_to.alert
            print("Cảnh báo hiện đang có.")
            return True
            
        except NoAlertPresentException:
            print("Không có cảnh báo hiện tại.")
            return False

    async def batDauXoa(self):
        try:
                
            wait = WebDriverWait(self.driver, 10)

            if(self.isOpen == True):
                #btn trở về home
                btn_home = wait.until(EC.element_to_be_clickable((By.XPATH,'/html/body/div[4]/div/div[2]/div[1]/div/div[2]/div/div[1]/button')))
                btn_home.click()  
            self.isOpen = True

            if(self.isAlert()):
                # Bạn có thể chấp nhận hoặc từ chối cảnh báo nếu cần
                self.alert.accept()  # Hoặc alert.dismiss() để từ chối

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

            #await asyncio.sleep(2)  # Thay vì time.sleep
            for log in self.logs:
                message = json.loads(log['message'])
                if ('Network.responseReceived' in message['message']['method'] and 
                    'Content-Disposition' in message['message']['params']['response']['headers'] and
                    'attachment' in message['message']['params']['response']['headers']['Content-Disposition']):
                    print("Tệp đang được tải xuống:", message['message']['params']['response']['url'])
                    await asyncio.sleep(1)

        finally:
            self.isend = True

        print("Quá trình tự động hóa đã hoàn thành.")