import requests

url1 = "https://fr.wikipedia.org/wiki/Ing%C3%A9nieur"
url2 = "https://fr.wikipedia.org/wiki/Dipl%C3%B4me"
url = "http://olympus.realpython.org/profiles/aphrodite"

def get_page(url):
    try:
        response = requests.get(url)
        html = response.text
        
        print(html)
        print("Status code: ", response.status_code)
    except Exception as e:
        print(f"An error occurred: {e}")
    
get_page(ur1);
print("========================Another page=========================")
get_page(url)