from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd
from datetime import datetime
import os
import sys

application_path=os.path.dirname(sys.executable)
now=datetime.now()
#DDMMYYYY
day_month_year=now.strftime("%d-%m-%Y")
driver = webdriver.Chrome()
driver.get("https://www.thesun.co.uk/sport/football")

wait = WebDriverWait(driver, 15)

# NEW selector
containers = wait.until(
    EC.presence_of_all_elements_located((By.XPATH, "//a[h3]"))
)

titles, subtitles, links = [], [], []

for c in containers:
    try:
        title = c.find_element(By.XPATH, ".//h3").text
    except:
        title = None

    try:
        subtitle = c.find_element(By.XPATH, ".//p").text
    except:
        subtitle = None

    link = c.get_attribute("href")

    titles.append(title)
    subtitles.append(subtitle)
    links.append(link)

df = pd.DataFrame({
     "subtitle": subtitles,
    "title": titles,
    "link": links
})
file_name=f'headline-{day_month_year}.csv'
final_path=os.path.join(application_path,file_name)
df.to_csv(final_path, index=False)
driver.quit()