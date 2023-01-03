import requests  # Get the url
from bs4 import BeautifulSoup  # Used for three traversal scraping in a webpage
from selenium import webdriver
import time


browser = webdriver.Firefox()

pdf_url = "https://view.publitas.com/billa-bulgaria/bg_weekly_digital_leaflet_22-12-28-12-2022__cw51__web/page/1"
browser.get(pdf_url)
time.sleep(3)
soup = BeautifulSoup(browser.page_source, 'html.parser')

li=soup.find_all('a', {'data-href': 'download_pdf'})
pdf_link = [i['href']  for i in li if i['href'].endswith('pdf')]
pdf_link = pdf_link[0].replace('\[', '').replace('\]', '')

# Get response object for link
response = requests.get(pdf_link)

# Write content in pdf file
pdf = open("billa_brochure" + ".pdf", 'wb')
pdf.write(response.content)
pdf.close()
print("File ", "billa_brochure", " downloaded")

