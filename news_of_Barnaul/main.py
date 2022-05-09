import requests
from bs4 import BeautifulSoup
import csv
import time

start_time = time.time()

headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36',
    'accept': '*/*'
}

url = 'https://barnaul-obr.ru'

def get_urls():

    with open('news.csv', 'w', encoding='utf-8-sig', newline='') as file:
        writer = csv.writer(file, delimiter=';')

        writer.writerow(
            (
                'Дата',
                'Название',
                'Полный текст новости в формате html',
                '1',
                '2',
                '3',
                '4',
                '5',
                '6',
                '7',
                '8',
                '9',
                '10'
            )
        )
    
    for i in range(1, 33):
        print(f'Страница {i} в работе')

        page_url = url + f'/news?News_page={i}'

        req = requests.get(url=page_url, headers=headers)
        soup = BeautifulSoup(req.text, 'lxml')

        news_urls = soup.find_all('li', class_='news__item')
        for item in news_urls:
            news_url =url + item.find('a').get('href').strip()
            get_data(url=news_url)

def get_data(url):

    news_data = []

    req = requests.get(url=url, headers=headers)
    soup = BeautifulSoup(req.text, 'lxml')

    news_items = soup.find('div', class_='news-item')

    try:
        news_date = news_items.find('div', class_='news-item__date').text.strip()
    except Exception as ex:
        news_date = 'Нет даты'

    try:
        news_title = news_items.find('div', class_='news-item__title').text.strip()
    except Exception as ex:
        news_title = 'Нет заголовка'

    try:
        news_full_text = news_items.find('div', class_='news-item__full-text').find_all('p')
    except Exception as ex:
        news_full_text = 'Нет полного текста новости'

    try:
        img_urls = news_items.find('div', class_='news-item__photos').find('ul', class_='preview-photos-small').find_all('li')
    except Exception as ex:
        pass

    try:
        img_1 = img_urls[0].find('img').get('src').strip()
    except Exception as ex:
        img_1 = ''

    try:
        img_2 = img_urls[1].find('img').get('src').strip()
    except Exception as ex:
        img_2 = ''

    try:
        img_3 = img_urls[2].find('img').get('src').strip()
    except Exception as ex:
        img_3 = ''

    try:
        img_4 = img_urls[3].find('img').get('src').strip()
    except Exception as ex:
        img_4 = ''

    try:
        img_5 = img_urls[4].find('img').get('src').strip()
    except Exception as ex:
        img_5 = ''

    try:
        img_6 = img_urls[5].find('img').get('src').strip()
    except Exception as ex:
        img_6 = ''

    try:
        img_7 = img_urls[6].find('img').get('src').strip()
    except Exception as ex:
        img_7 = ''

    try:
        img_8 = img_urls[7].find('img').get('src').strip()
    except Exception as ex:
        img_8 = ''

    try:
        img_9 = img_urls[8].find('img').get('src').strip()
    except Exception as ex:
        img_9 = ''

    try:
        img_10 = img_urls[9].find('img').get('src').strip()
    except Exception as ex:
        img_10 = ''

    news_data.append(
        {
            'Дата': news_date,
            'Название': news_title,
            'Полный текст новости в формате html':  news_full_text,
            '1': img_1,
            '2': img_2,
            '3': img_3,
            '4': img_4,
            '5': img_5,
            '6': img_6,
            '7': img_7,
            '8': img_8,
            '9': img_9,
            '10': img_10
        }
    )

    with open('news.csv', 'a', encoding='utf-8-sig', newline='') as file:
        writer = csv.writer(file, delimiter=';')
        writer.writerow(
            (
                news_date,
                news_title,
                news_full_text,
                img_1,
                img_2,
                img_3,
                img_4,
                img_5,
                img_6,
                img_7,
                img_8,
                img_9,
                img_10
            )
        )
    

def main():
    get_urls()
    finish_time = time.time() - start_time
    print(f"Затраченное на работу скрипта время: {finish_time}")

if __name__ == '__main__':
    main()