import requests
from bs4 import BeautifulSoup

url1 = "https://fr.wikipedia.org/wiki/Ing%C3%A9nieur"
url2 = "https://fr.wikipedia.org/wiki/Dipl%C3%B4me"
url = "http://olympus.realpython.org/profiles/aphrodite"

def get_page(url):
    try:
        response = requests.get(url)
        html = response.text
        
        soup = BeautifulSoup(html, 'html.parser')
        text = soup.get_text()
        words = set(text.split())
        
        print("Words on the page without HTML tags and without duplicates:")
        print(words)
        print("Status code: ", response.status_code)
    except Exception as e:
        print(f"An error occurred: {e}")
    
get_page(url1)
print("========================Another page=========================")
get_page(url)