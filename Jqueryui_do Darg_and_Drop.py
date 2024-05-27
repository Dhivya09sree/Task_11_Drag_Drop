from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import os
from selenium.webdriver.common.action_chains import ActionChains


class Darg_and_drop :
    def __init__(self):
        self.driver = None
        self.wait_timeout = 15

    # Initialize the ChromeDriver
    def initialize_driver(self):
        service = Service(ChromeDriverManager().install())
        # Create a new instance of the Chrome driver
        self.driver = webdriver.Chrome(service=service)
        self.wait = WebDriverWait(self.driver, self.wait_timeout)

    # Open a website
    def open_website(self, url):
        self.driver.get(url)

   # Maximize the browser window
    def maximize_window(self):
        self.driver.maximize_window()

    # Switch to the iframe that contains the draggable and droppable elements
    def Switch_to_the_iframe(self):
       iframe = self.driver.find_element(By.CSS_SELECTOR, ".demo-frame")
       self.driver.switch_to.frame(iframe)

# Locate the draggable and droppable elements
    def draggable_and_droppable(self):
       draggable = self.driver.find_element(By.ID, "draggable")
       droppable = self.driver.find_element(By.ID, "droppable")

        # Perform drag and drop operation
       actions = ActionChains(self.driver)
       actions.drag_and_drop(draggable, droppable).perform()

       # Wait to observe the result
       time.sleep(3)

       # Print the text of the droppable element to confirm the drop
       print(droppable.text)

       # Print confirmation
       print("Drag and drop operation performed successfully.")

    def close(self):
        self.driver.close()


    def close(self):
        self.driver.close()

# Create object
Darg = Darg_and_drop()

# Initialize the browser
Darg.initialize_driver()

# Navigate to URL
Darg.open_website("https://jqueryui.com/droppable/")
time.sleep(3)

# Maximize the window
Darg.maximize_window()

# Switch to iframe
Darg.Switch_to_the_iframe()

# using Action class  perfom draggable_and_droppable
Darg.draggable_and_droppable()
# Close the browser
Darg.close()

