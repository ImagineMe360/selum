from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By


def test_homepage_element():
    options = Options()
    options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")

    driver = webdriver.Chrome(options=options)
    driver.get("http://localhost:5173")  # runs locally in GitHub Actions

    element = driver.find_element(By.ID, "home-title")
    assert "Welcome" in element.text

    print("✅ Home page title element found:", element.text)
    driver.quit()
