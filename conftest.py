from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest

@pytest.fixture(scope='module')
def driver():
    chrome_options = Options()
    # chrome_options.add_argument("--headless")
    # chrome_options.add_argument("--disable-gpu")
    # chrome_options.add_argument("--window-size=1920x1018")
    # chrome_options.add_argument("--no-sandbox")
    driver = webdriver.Chrome(options=chrome_options)
    driver.maximize_window()
    driver.implicitly_wait(10)
    yield driver
    driver.quit()

@pytest.fixture(scope="function")
def login(driver):
    driver.get('https://tutorialsninja.com/demo/index.php?route=account/login')

    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'input-email')))

    driver.find_element(By.ID, 'input-email').send_keys('christine.voskerchyan@gmail.com')  # Replace with valid email
    driver.find_element(By.ID, 'input-password').send_keys('123456789')  # Replace with valid password

    driver.find_element(By.CSS_SELECTOR, 'input[type="submit"]').click()

    WebDriverWait(driver, 10).until(EC.title_contains("My Account"))

