from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.common.keys import Keys


def test_homepage_element():
    options = Options()
    options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")

    driver = webdriver.Chrome(options=options)
    driver.get("http://localhost:5173")  # runs locally in GitHub Actions

    # Wait and find the element by ID
    element = driver.find_element(By.ID, "home-title")
    assert "My To-Do App" in element.text

    print("✅ Home page title element found:", element.text)
    driver.quit()


def test_add_todo_item():
    options = Options()
    options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")

    driver = webdriver.Chrome(options=options)
    driver.get("http://localhost:5173")

    # Locate input and button
    input_field = driver.find_element(By.ID, "task-input")
    add_button = driver.find_element(By.ID, "add-task-btn")

    # Type a task and click add
    task_text = "Buy groceries"
    input_field.send_keys(task_text)
    add_button.click()

    # Wait briefly to allow UI to update
    time.sleep(1)

    # Check if task appears in the list
    task_list = driver.find_element(By.ID, "task-list")
    assert task_text in task_list.text
    print(f"✅ Task successfully added: {task_text}")

    driver.quit()


test_add_todo_item()
