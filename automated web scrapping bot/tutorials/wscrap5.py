import urllib.request

#URL of the web page we want to fetch:
url = 'https://www.example.com'

try:
    #open the URL and read its content
    response = urllib.request.urlopen(url)

    #read the cotent of the response
    data = response.read()

    #decode the data (if it's in bytes) to a string
    html_content = data.decode('utf-8')

    #print the HTML content of the web page
    print(html_content)
except Exception as e:
    print('Error fetching URL:', e)

