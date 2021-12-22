from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class whatsbot(webdriver.Chrome):
    def __init__(self,driver_path):
        self.chrome_options=webdriver.ChromeOptions()
        self.chrome_options.add_experimental_option("excludeSwitches",["enable-logging"])
        super().__init__(driver_path,options=self.chrome_options)
        self.get("https://web.whatsapp.com/")
        self.implicitly_wait(30)

    def search_chat(self,chat_name):
        try:
            self.chat=self.find_element_by_css_selector(f"[title~={chat_name}]")
            self.chat.click()
            return True
        except:
            return False
    
    def search_by_bar(self,bar_chatname):
        try:
            self.search_bar=self.find_element_by_xpath("/html/body/div[1]/div[1]/div[1]/div[3]/div/div[1]/div/label/div/div[2]")
            self.search_bar.click()
            self.search_bar.send_keys(bar_chatname)
            self.chat_result=self.search_chat(bar_chatname)
            return self.chat_result
        except:
            return False

    def send_msg(self,msg):
        try:
            self.send_msg_chat=self.find_element_by_xpath("/html/body/div[1]/div[1]/div[1]/div[4]/div[1]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[2]")
            self.send_msg_chat.send_keys(msg)
            self.btn_send=self.find_element_by_css_selector(f"[data-icon~=send]")
            self.btn_send.click()
            return True
        except:
            return False
