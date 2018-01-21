import requests, urllib.request
from bs4 import BeautifulSoup

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
                         'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.84 Safari/537.36'}

for url in open('urls.txt', 'r'):
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.content, 'html.parser')

    img = soup.find("div", id="gallery-content").find('img')
    link = img.get('src')

    def load_img(url):
        name = url.split('/')[4]+'.png'
        urllib.request.urlretrieve(url, name)

    load_img(link)



