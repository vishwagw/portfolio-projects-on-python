#1.For Firefox:
#from selenium import webdriver

#create web driver object
#driver = webdriver.Firefox()

#now, ge google.co.in
#driver.get("https://google.co.in / search?q = geeksforgeeks")

#2.For chrome:
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDrivermanager

#for holding the result list:
elements_list = []

for page in range(1, 3, 1):
    page_url = "https://webscraper.io/test-sites/e-commerce/static/computers/laptops?page=" + str(page)
    driver = webdriver.Chrome(ChromeDrivermanager().install())
    driver.get(page_url)
    title = driver.find_elements(By.CLASS_NAME, 'title')
    price = driver.find_elements(By.CLASS_NAME, 'price')
    description = driver.find_elements(By.CLASS_NAME, 'description')
    rating = driver.find_elements(By.CLASS_NAME, 'ratings')

    for i in range(len(title)):
        elements_list.append([title[i].text, price[i].text, description[i].text, rating[i].text])

print(elements_list)

#closing the driver
driver.close()

