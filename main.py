import requests
from bs4 import BeautifulSoup

soup = BeautifulSoup(r.content, 'html.parser')
url = 'https://www.allsides.com/media-bias/media-bias-ratings'

r = requests.get(url)

print(r.content[:100])

def save_html(html, path):
    with open(path, 'wb') as f:
        f.write(html)
    
save_html(r.content, 'google_com') 