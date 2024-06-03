import requests
from bs4 import BeautifulSoup

url1 = "https://fr.wikipedia.org/wiki/Ing%C3%A9nieur"
url2 = "https://fr.wikipedia.org/wiki/Dipl%C3%B4me"
url3 = "https://fr.wikipedia.org/wiki/Informatique"


def get_page_words(url):
    try:
        response = requests.get(url)
        html = response.text
        
        soup = BeautifulSoup(html, 'html.parser')
        text = soup.get_text()
        words = set(text.split())
        
        print("Words on the page without HTML tags and without duplicates:")
        print(words)
        
        return words
    except Exception as e:
        print(f"An error occurred: {e}")
    
words_url1 = get_page_words(url1)
words_url2 = get_page_words(url2)
words_url3 = get_page_words(url3)


with open('wordlist.txt', 'w', encoding='utf-8') as file:
    for word in words_from_dummy_url:
        file.write(f"{word}\n")
print("Wordlist has been created successfully")