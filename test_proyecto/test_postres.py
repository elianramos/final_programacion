import unittest
from selenium import webdriver
from selenium.webdriver.edge.options import Options
import os
import HtmlTestRunner

class TestPostres(unittest.TestCase):
    def setUp(self):
        edge_options = Options()
        edge_options.add_argument("--disable-gpu")
        edge_options.add_argument("--no-sandbox")
        edge_options.add_argument("--disable-dev-shm-usage")

        self.driver = webdriver.Edge(options=edge_options)
        self.driver.get("file:///C:/Users/elian/OneDrive/Documentos/final-proyecto/index.html") 

    def test_navegar_a_postres(self):
        driver = self.driver

        self.assertIn("index.html", driver.current_url)

        self.navegar_y_capturar_screenshot("postres.html", "postres_page")

    def navegar_y_capturar_screenshot(self, archivo_html, page_name):
        driver = self.driver
        

        driver.get(f"file:///C:/Users/elian/OneDrive/Documentos/final-proyecto/{archivo_html}")


        driver.implicitly_wait(10)  


        self._guardar_screenshot(page_name)

    def _guardar_screenshot(self, page_name):

        if not os.path.exists('resultado_img'):
            os.makedirs('resultado_img')  
        screenshot_path = f'resultado_img/{page_name}_screenshot.png'
        self.driver.save_screenshot(screenshot_path)
        print(f"Screenshot guardado en {screenshot_path}")

    def tearDown(self):

        self.driver.quit()

if __name__ == "__main__":

    test_runner = HtmlTestRunner.HTMLTestRunner(output="resultados")
    unittest.main(testRunner=test_runner)
