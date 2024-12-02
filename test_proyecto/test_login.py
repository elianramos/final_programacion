import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os
import HtmlTestRunner

class TestLogin(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()  
        self.driver.get("file:///C:/Users/elian/OneDrive/Documentos/final-proyecto/login.html")

        self.driver.execute_script("""
            localStorage.setItem('userEmail', 'testuser@example.com');
            localStorage.setItem('userPassword', 'Test1234!');
        """)

    def test_login(self):
        driver = self.driver


        email_input = driver.find_element(By.ID, "loginEmail")
        password_input = driver.find_element(By.ID, "loginPassword")
        submit_button = driver.find_element(By.CSS_SELECTOR, "button[type='submit']")

        email_input.send_keys("testuser@example.com")
        password_input.send_keys("Test1234!")
        submit_button.click()

        try:
            WebDriverWait(driver, 5).until(
                EC.url_contains("file:///C:/Users/elian/OneDrive/Documentos/final-proyecto/index.html") 
            )
            print("Redirección exitosa.")
        except Exception as e:
            self.fail(f"La redirección falló: {e}")

    def tearDown(self):
        if not os.path.exists('resultado_img'):
            os.makedirs('resultado_img')

        screenshot_path = 'resultado_img/test_login_screenshot.png'
        self.driver.save_screenshot(screenshot_path)
        print(f"Captura de pantalla guardada en {screenshot_path}")

        self.driver.quit()

if __name__ == "__main__":
    test_runner = HtmlTestRunner.HTMLTestRunner(output="resultados")
    unittest.main(testRunner=test_runner)
