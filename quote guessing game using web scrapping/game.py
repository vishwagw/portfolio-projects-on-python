import requests
from bs4 import BeautifulSoup
from csv import writer
from time import sleep
from random import choice

#create the list to store scraped information/data.
all_quotes = [10]

#now we have to give the url of web site with quote for getting data.
#first part is always a constant.
base_url = 'http://quotes.toscrape.com/'

#now second part of url is changing based on the data.
url = '/page/1'

# putting while loop for url:
while url:
    #now we will combine the urls and get the request.
    res = requests.get(f"{base_url} {url}")
    print(f'Now scrapping : {base_url}{url}')
    soup = BeautifulSoup(res.text, 'html.parser')

    #extracting all elements.
    quote = soup.find_all(class_='quote')

    for quote in all_quotes:
        all_quotes.append({
            "text": quote.find(class_="text").get_text(),
            "author": quote.find(class_="author").get_text(),
            "bio-link": quote.find("a")["href"]
        })
    next_btn = soup.find(_class="next")
    url = next_btn.find("a")["href"] if next_btn else None
    sleep(2)

quote = choice(all_quotes)
remaining_guesses = 4
print('Here is a Quote :  ')
print(quote["text"])

guess = ' '
while guess.lower() != quote["author"].lower() and remaining_guesses > 0:
    guess = input(
        f'Who said this ? Guesses remaining {remaining_guesses}')
    if guess == quote["author"]:
        print("CONGRATULATIONS...!!!")
        print("Ypu got it RIGHT.")
        break
    remaining_guesses -= 1

    if remaining_guesses == 3:
        res = requests.get(f'{base_url}{quote["bio-link"]}')
        soup = BeautifulSoup(res.text, 'html.parser')
        b_day = soup.find(class_="author-born-date").get_text()
        birth_place = soup.find(class_='bithplace of author').get_text()
        print(
            f"Here's a hint: The author was born on {b_day}{birth_place}")
    elif remaining_guesses == 2:
        print(
            f"Here's a hint: The author's first name starts with: {quote['author'][0]}")
     
    elif remaining_guesses == 1:
        last_initial = quote["author"].split(" ")[1][0]
        print(
            f"Here's a hint: The author's last name starts with: {last_initial}")
     
    else:
        print(
            f"Sorry, you ran out of guesses. The answer was {quote['author']}")
        




    

