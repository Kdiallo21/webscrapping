import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Define ChromeDriver service
service = Service('C:\Users\Student\Desktop\web\chromedriver-win64\chromedriver.exe')
driver = webDriver.Chrome(service=service)

# Load the webpage
driver.get('https://www.yearupalumni.org/s/1841/interior.aspx?sid=1841&gid=2&pgid=440')

# Wait for the page to fully load
time.sleep(5)  # Optional, replace with explicit wait if needed

# Parse the page source with BeautifulSoup
content = driver.page_source
soup = BeautifulSoup(content, 'html.parser')

# Close the driver after fetching the content
driver.quit()

# Extract the data
results = []
for element in soup.findAll(attrs={'title': True}):  # Find elements with a title attribute
    name = element.find('a')
    if name and name.text not in results:
        results.append(name.text)

# Save results to a CSV
if results:
    df = pd.DataFrame({'Names': results})
    df.to_csv('names.csv', index=False, encoding='utf-8')
    print("Data saved to names.csv")
else:
    print("No data found!")
