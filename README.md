### WhatsApp Mass Messaging Without Storing Contacts

This Python script automates sending WhatsApp messages via the WhatsApp web application without needing to save contact numbers. It's designed to efficiently send configured messages to recipients, using data sourced from an Excel sheet. The script's capability is ideal for distributing advertisements or bulk messages.

## Requirements
To successfully run this Python script, ensure that your system meets the following prerequisites. It's important to note that contact numbers need not be saved in your phone. Note that currently only text messages are supported.

Python 3.8: Download from Python's official website.
Chrome v79: Download from Google Chrome's official website.
Pandas: Install via command prompt using pip install pandas.
Xlrd: Install via command prompt using pip install xlrd.
Selenium: Install via command prompt using pip install selenium.
Web Driver: Install via command prompt using pip install webdriver_manager.
Openpyxl: Install via command prompt using pip install openpyxl.
Implementation
Begin by cloning this repository.
Execute the Python script named script.py in the terminal using the command "py script.py".
The script initiates WhatsApp web through Chrome.
Scan the QR code displayed with your phone.
Proceed by entering commands into the command prompt to continue.
The script sends messages using URLs that include contact numbers and messages retrieved from the Excel sheet.
Once all messages have been sent, the Chrome driver will automatically close.

Legal Disclaimer
This code is independent and unofficial, and it is not affiliated with, authorized, maintained, sponsored, or endorsed by WhatsApp or any of its affiliates or subsidiaries. Users are advised to use this software at their own risk. Commercial usage of this code/repository is strictly prohibited.
