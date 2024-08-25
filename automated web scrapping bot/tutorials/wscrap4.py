from lxml import html
import requests

#define the url of the website to scrape.
url = 'https://example.com'

#now we are sending a HTTP request to the website and retrieve the HTML content.
response = requests.get(url)

#now we parse the HTML, content using the Lxml.
tree = html.fromstring(response.content)

#Extract specific elements from the HTML tree using Xpath.
#For example, let's extract the titles of all the links on the page.
link_titles = tree.xpath('//a/text()')

#print the extracted files
for title in link_titles:
    print(title)

