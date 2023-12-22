# Instagram-Automation-using-Selenium

This Python script uses Selenium, a web automation library, to demonstrate a simple login and logout sequence on Instagram.

### Setup and Requirements

- **Python:** Ensure Python is installed on your system. This code was written using Python 3.
- **Selenium:** Install Selenium using `pip install selenium`.
- **Web Browser:** The script uses Microsoft Edge as the browser. Ensure you have Microsoft Edge installed on your system.
- **WebDriver:** Download the appropriate WebDriver for Microsoft Edge from [here](https://developer.microsoft.com/en-us/microsoft-edge/tools/webdriver/) and place it in your system's PATH or specify its location in the code.

### Usage

1. **Clone Repository:** Clone this repository to your local machine.
2. **Install Dependencies:** Install the required dependencies using `pip install -r requirements.txt`.
3. **Setup WebDriver:** Ensure the WebDriver for Microsoft Edge is correctly set up.
4. **Run the Script:** Execute the Python script `instagram_automation.py`.
5. **Credentials:** Replace `<Your Username>` and `<Your Password>` with your Instagram credentials in the script before running it.

### File Description

- `instagram_automation.py`: Python script that automates the login and logout process on Instagram using Selenium.
- `README.md`: This file providing instructions and information about the script.

### Important Notes

- **Security:** Avoid hardcoding sensitive information like passwords directly in the code.
- **Wait Times:** Adjust the wait times (`time.sleep()`) based on your system's speed and internet connection for effective automation.
- **XPath:** The script uses XPath to locate elements. Ensure the XPath is updated if Instagram's structure changes.

### Disclaimer

This script is for educational purposes and demonstrates basic web automation using Selenium. Use it responsibly and in compliance with Instagram's terms of service to avoid any account-related issues.
