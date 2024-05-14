from urllib.request import urlopen
import ssl
ssl._create_default_https_context = ssl._create_unverified_context

url1 = "https://fr.wikipedia.org/wiki/Ing%C3%A9nieur"
url2 = "https://fr.wikipedia.org/wiki/Dipl%C3%B4me"
url = "http://olympus.realpython.org/profiles/aphrodite"

try:
    page = urlopen(url1)
    html_bytes = page.read()
    html = html_bytes.decode("utf-8")
    print(html)
except Exception as e:
    print(f"An error occurred: {e}")
