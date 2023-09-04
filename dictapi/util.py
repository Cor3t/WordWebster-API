import requests
from bs4 import BeautifulSoup

def get_word_meaning(query):

    url = f"https://merriam-webster.com/dictionary/{query}"
    response = requests.get(url)

    contents = BeautifulSoup(response.text, features='html.parser')
    containers = contents.find_all('div', class_='entry-word-section-container')

    for container in containers:
        words = [word.text for word in container.find_all('span', class_='dtText')]

        return [word.strip(': ').capitalize() for word in words]
