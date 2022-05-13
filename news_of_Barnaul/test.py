import requests
from bs4 import BeautifulSoup

headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36',
    'accept': '*/*'
}

url = 'https://reg.o-time.ru/start.php?event=22191'

req = requests.get(url=url, headers=headers).content
soup = BeautifulSoup(req, 'html.parser')
# print(soup)

# with open('index.html', 'w', encoding='utf-8-sig') as file:
#     file.write(soup.text)

item = soup.find('div', class_='results1').find('div', class_='rname').text.strip()
print(item)