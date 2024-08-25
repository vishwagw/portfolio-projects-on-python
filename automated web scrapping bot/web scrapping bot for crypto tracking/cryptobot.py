#importing the libraries
import requests
from bs4 import BeautifulSoup
from datetime import datetime
import time

#now we are going to get the url data and parse the HTML code.
url = 'https://coinmarketcap.com/'
response = requests.get(url)
text = response.text
data = BeautifulSoup(text, 'html.parser')

#after that we are moving to exteact data from the web site.
#Heading is in the top of a web page.
#so, we are going to get the heading first.
headings = data.find_all('tr')[0]
headings_list = [] 

for x in headings:
    headings_list.append(x.text)

#we only requestig for first few colomns.In this case, we request first 10 colomns.
headings_list = headings_list[:10]

#Now we are going to print the results.
print('Headings are: ')
for column in headings_list:
    print(column)

#after columns are scrapped, now we are going for the rows.
#We can deicde how many rows, we need.(in this case how many cryptocurrencies we need to scrap information.)
for x in range(1, 11):
    table = data.find_all('tr')[x]
    c = table.find_all('td')

    for x in c:
        print(x.text, end=' ')
    print('')



