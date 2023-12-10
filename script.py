import pandas as pd
from time import sleep
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By

# Read data from the Excel file into a pandas DataFrame
excel_data = pd.read_excel('test.xlsx')

# Initialize counter for iterating through the Excel data
count = 0

# Initialize Chrome WebDriver
driver = webdriver.Chrome()

# Open WhatsApp Web
driver.get('https://web.whatsapp.com')

# Prompt user to press ENTER after logging into WhatsApp Web and chats are visible
input("Press ENTER after logging into WhatsApp Web and your chats are visible.")

# Iterate through the 'Contact' column in the Excel data to send messages
for contact, message in zip(excel_data['Contact'], excel_data['Message']):
    try:
        # Construct the URL with the phone number and message for each contact
        url = 'https://web.whatsapp.com/send?phone={}&text={}'.format(contact, message)
        sent = False

        # It tries 3 times to send a message in case any error occurred
        driver.get(url)

        try:
            # Wait until the 'Send' button is clickable
            click_btn = WebDriverWait(driver, 35).until(EC.element_to_be_clickable((By.CLASS_NAME, '_3XKXx')))
        except Exception as e:
            print(f"Sorry, message could not be sent to {contact}")
        else:
            # Add a delay for stability before clicking the 'Send' button
            sleep(2)
            click_btn.click()
            sent = True
            sleep(5)
            print(f"Message sent to: {contact}")

    except Exception as e:
        # If there's an error, print a failure message
        print(f"Failed to send message to {contact}: {e}")

# Close the WebDriver after sending messages to all contacts
driver.quit()

# Print a completion message
print("The script executed successfully.")
