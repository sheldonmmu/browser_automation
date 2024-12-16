# cheatsheet https://github.com/mherrmann/helium/blob/master/docs/cheatsheet.md
# repo https://github.com/mherrmann/helium/tree/master

from helium import *
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Start Chrome and navigate to the MMU Library website
driver = start_chrome("https://www.mmu.ac.uk/library")

# Handle cookie consent if it appears
cookie_buttons = ['Reject non-essential', 'I accept', 'I agree', 'Accept all']
for button in cookie_buttons:
    if Text(button).exists():
        click(button)
        break

time.sleep(5)

# Wait for the search input to be present in the DOM
wait = WebDriverWait(driver, 10)
search_input = wait.until(EC.presence_of_element_located((By.NAME, "queryString")))

# Scroll the element into view
driver.execute_script("arguments[0].scrollIntoView();", search_input)

# Use Helium's write function to enter text
write('business management', into=S('input[type="search"]'))

# Press Enter to submit the search
press(ENTER)