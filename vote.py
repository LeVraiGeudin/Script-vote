# Vérifiez que Selenium est correctement installé
import selenium
print("Selenium version:", selenium.__version__)

# Exemple de script Selenium
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Chemin vers ChromeDriver
CHROMEDRIVER_PATH = 'C:\\Users\\cante\\Desktop\\chromedriver-win64\\chromedriver.exe'

# Configurer les options pour le navigateur
chrome_options = Options()
chrome_options.add_argument("--headless")

driver = None
try:
    driver = webdriver.Chrome(service=Service(CHROMEDRIVER_PATH), options=chrome_options)
    driver.get('https://example.com')
    print("Page ouverte avec succès.")
    
    wait = WebDriverWait(driver, 10)
    element = wait.until(EC.visibility_of_element_located((By.TAG_NAME, 'h1')))
    print("Élément trouvé :", element.text)

except Exception as e:
    print(f"Erreur : {e}")

finally:
    if driver:
        driver.quit()
        print("Navigateur fermé.")
