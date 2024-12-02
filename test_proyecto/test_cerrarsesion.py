import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os
import HtmlTestRunner

class TestLogout(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome() 
        self.driver.get("file:///C:/Users/elian/OneDrive/Documentos/final-proyecto/index.html")  

    def test_logout_button(self):
        driver = self.driver


        try:
            user_button = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.ID, "userButton"))
            )
            user_button.click()  


            logout_button = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.ID, "sesioncerrar"))
            )
            
            self.assertTrue(logout_button.is_displayed(), "El botón de cerrar sesión no es visible.")
            logout_button.click()  

            WebDriverWait(driver, 5).until(
                EC.url_contains("file:///C:/Users/elian/OneDrive/Documentos/final-proyecto/login.html")
            )
            print("Redirección exitosa a la página de login.")
        except Exception as e:
            self.fail(f"La redirección falló o el botón no está clickeable: {e}")

    def tearDown(self):

        if not os.path.exists('resultado_img'):
            os.makedirs('resultado_img')

        screenshot_path = 'resultado_img/test_logout_screenshot.png'
        self.driver.save_screenshot(screenshot_path)
        print(f"Captura de pantalla guardada en {screenshot_path}")


        self.driver.quit()

if __name__ == "__main__":

    test_runner = HtmlTestRunner.HTMLTestRunner(output="resultados")
    unittest.main(testRunner=test_runner)
