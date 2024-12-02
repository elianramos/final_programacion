import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import os
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.alert import Alert
from datetime import datetime
import HtmlTestRunner 

class TestRegistro(unittest.TestCase):
    def setUp(self):
       
        chrome_options = Options()
        self.driver = webdriver.Chrome(options=chrome_options)

        
        self.driver.get("C:\\Users\\elian\\OneDrive\\Documentos\\final-proyecto\\register.html")

    def test_registro_exitoso(self):
        driver = self.driver
        wait = WebDriverWait(driver, 10)

        
        username_input = driver.find_element(By.ID, "registerUsername")
        email_input = driver.find_element(By.ID, "registerEmail")
        password_input = driver.find_element(By.ID, "registerPassword")
        submit_button = driver.find_element(By.CSS_SELECTOR, "button[type='submit']")

        
        username_input.send_keys("testus")
        email_input.send_keys("elian12@gmail.com")
        password_input.send_keys("elian12")

        
        submit_button.click()

        
        try:
            
            alert = wait.until(EC.alert_is_present())
            alert_text = alert.text
            print(f"Alerta detectada: {alert_text}")
            alert.accept()  
        except:
            print("No se detectaron alertas inesperadas tras el envío del formulario.")

        
        screenshot_folder = 'resultado_img'
        if not os.path.exists(screenshot_folder):
            os.makedirs(screenshot_folder) 

        screenshot_path = os.path.join(screenshot_folder, f"registro_test_{datetime.now().strftime('%Y%m%d_%H%M%S')}.png")
        driver.save_screenshot(screenshot_path)

        
        print(f"Test completado con éxito. Screenshot guardado en {screenshot_path}")

    def tearDown(self):
        
        self.driver.quit()

if __name__ == "__main__":
    
    test_runner = HtmlTestRunner.HTMLTestRunner(output="resultados") 

   
    unittest.main(testRunner=test_runner)