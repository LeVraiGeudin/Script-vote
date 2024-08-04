from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import time

# Chemin vers le WebDriver
CHROMEDRIVER_PATH = 'C:\\Users\\cante\\Desktop\\chromedriver-win64\\chromedriver.exe'  # Assure-toi que ce chemin est correct

# Configurer les options pour le navigateur
chrome_options = Options()
# Décommenter cette ligne pour exécuter le navigateur en mode visible
# chrome_options.add_argument("--headless")

driver = None
try:
    # Créer une instance du navigateur
    driver = webdriver.Chrome(service=Service(CHROMEDRIVER_PATH), options=chrome_options)

    # Ouvrir la page de vote
    driver.get('https://top-serveurs.net/dayz/vote/creality-dayz')
    print("Page ouverte avec succès.")

    # Attendre et cliquer sur le bouton d'autorisation
    wait = WebDriverWait(driver, 10)
    consent_button = wait.until(EC.element_to_be_clickable((By.XPATH, '//button[contains(@class, "fc-cta-consent") and .//p[contains(text(), "Autoriser")]]')))
    print("Bouton d'autorisation trouvé avec succès.")
    consent_button.click()
    print("Clic sur le bouton d'autorisation effectué.")

    # Attendre que la page de vote soit complètement chargée après le clic sur le bouton d'autorisation
    time.sleep(3)  # Ajuste ce délai si nécessaire

    # Attendre que le champ pseudo soit présent et interactif
    pseudo_field = wait.until(EC.visibility_of_element_located((By.NAME, 'playername')))
    print("Champ pseudo trouvé avec succès.")

    # Entrer le pseudo
    pseudo_field.send_keys('LeVraiGeudin')
    print("Pseudo entré avec succès.")

    # Attendre que le bouton de vote soit visible et cliquable
    vote_button = wait.until(EC.element_to_be_clickable((By.XPATH, '//button[contains(@class, "btn-submit-vote") and contains(text(), "Voter")]')))
    print("Bouton de vote trouvé avec succès.")
    
    # Faire défiler jusqu'au bouton de vote
    driver.execute_script("arguments[0].scrollIntoView(true);", vote_button)
    
    # Déboguer avant le clic
    if vote_button.is_displayed() and vote_button.is_enabled():
        # Utiliser ActionChains pour le clic
        actions = ActionChains(driver)
        actions.move_to_element(vote_button).click().perform()
        print("Clic sur le bouton de vote effectué.")
    else:
        print("Le bouton de vote n'est pas cliquable.")
    
    # Attendre quelques secondes pour s'assurer que le vote est bien pris en compte
    time.sleep(5)

    print("Vote enregistré avec succès.")

except Exception as e:
    print(f"Erreur lors de l'envoi du vote: {e}")

finally:
    # Fermer le navigateur, si driver est défini
    if driver:
        driver.quit()
        print("Navigateur fermé.")
