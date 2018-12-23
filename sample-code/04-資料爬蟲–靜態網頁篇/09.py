import requests
from bs4 import BeautifulSoup

url = 'https://www.ptt.cc/bbs/Beauty/index.html'
r = requests.get(url)

soup = BeautifulSoup(r.text, "html5lib")

for d in soup.find_all(class_="title"):
    print(d.text.replace('\t', '').replace('\n', ''))
    try:
        r = BeautifulSoup(requests.get('https://www.ptt.cc'+d.find('a')['href']).text, "html5lib")
        print('作者: ' + r.find(class_='article-meta-value').text)
    except:
        continue
