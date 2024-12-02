import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.edge.options import Options
import os
import HtmlTestRunner
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TestCarritoRedireccion(unittest.TestCase):

    def setUp(self):
 
        edge_options = Options()
        edge_options.add_argument("--disable-gpu")
        edge_options.add_argument("--no-sandbox")
        edge_options.add_argument("--disable-dev-shm-usage")


        self.driver = webdriver.Edge(options=edge_options)
        self.driver.get("file://C:/Users/elian/OneDrive/Documentos/final-proyecto/index.html")  
    def test_redireccion_carrito(self):
        driver = self.driver


        boton_carrito = driver.find_element(By.CLASS_NAME, "fa-headset")  
        boton_carrito.click()


        WebDriverWait(driver, 10).until(lambda d: d.current_url.endswith("soporte.html"))

        self.assertTrue(driver.current_url.endswith("soporte.html"))
        print("Redirección exitosa al soporte.")

        self._guardar_screenshot("redireccion_soporte")

    def _guardar_screenshot(self, nombre_pagina):
  
        if not os.path.exists('resultados_img'):
            os.makedirs('resultados_img')

        screenshot_path = f'resultados_img/{nombre_pagina}_screenshot.png'
        self.driver.save_screenshot(screenshot_path)
        print(f"Screenshot guardado en {screenshot_path}")

    def tearDown(self):

        self.driver.quit()

if __name__ == "__main__":
    test_runner = HtmlTestRunner.HTMLTestRunner(output="resultados")
    unittest.main(testRunner=test_runner)
