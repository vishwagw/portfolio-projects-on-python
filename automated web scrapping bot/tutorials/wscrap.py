import requests
from bs4 import BeautifulSoup

#We have imported the library.
#Now, we have to make a GET requests. 
r = requests.get('https://www.geeksforgeeks.org/python-programming-language/')

#Now, we have to look at the response that we have recieved.
#success code - 200

#print(r.content)

#Now with beautifulsoup, we are goin to parse the items.

soup = BeautifulSoup(r.content, 'html.parser')
print(soup.prettify())




