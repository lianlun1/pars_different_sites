import requests
from bs4 import BeautifulSoup
import csv

headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36',
    'accept': '*/*'
}

def get_url_data(slug_number):
    url = f'https://reg.o-time.ru/start.php?event={slug_number}'

    with open(f'{slug_number}.csv', 'w', encoding='utf-8-sig', newline='') as file:
        writer = csv.writer(file, delimiter=';')
        writer.writerow(
            (
                'Место',
                'Стартовый номер',
                'Фамилия Имя',
                'результат Ган Тайм',
                'Рузельтат Чип Тайм',
                'Возрастная група',
                'Дистанция'
            )
        )

    try:
        request = requests.get(url=url, headers=headers).content
        soup = BeautifulSoup(request, 'html.parser')

        options = soup.find('div', class_='step1center').find_all('option')

        for option in options:
            url = option.get('value')
            option = option.text.strip()
            
            request = requests.get(url=url, headers=headers).content
            soup = BeautifulSoup(request, 'html.parser')

            get_items(soup=soup, option=option, slug_number=slug_number)
    except Exception as ex:
        print(ex)

def get_items(soup, option, slug_number):

    results_data = []

    for i in range(1, 3):
        result_items = soup.find_all('div', class_=f'results{i}')

        for item in result_items:

            try:
                rank = item.find('div', class_='rank').text.strip()
            except:
                rank = ''

            try:
                rbib = item.find('div', class_='rbib').text.strip()
            except:
                rbib = ''

            try:
                name = item.find('div', class_='rname').find('b').text.strip()
            except:
                name = ''

            try:
                gruntime = item.find('div', class_='rres').text.strip()
                g = gruntime.split(' ')
                guntime = g[0]
                runtime = g[1]
            except:
                guntime = ''
                runtime = ''

            try:
                rank_a = item.find('div', class_='rank_a').text.strip()
            except:
                rank_a = ''

            results_data.append(
                {
                    'Место': rank,
                    'Стартовый номер': rbib,
                    'Фамилия Имя': name,
                    'результат Ган Тайм': guntime,
                    'Рузельтат Чип Тайм': runtime,
                    'Возрастная група': rank_a,
                    'Дистанция': option
                }
            )

            with open(f'{slug_number}.csv', 'a', encoding='utf-8-sig', newline='') as file:
                writer = csv.writer(file, delimiter=';')
                writer.writerow(
                    (
                        rank,
                        rbib,
                        name,
                        guntime,
                        runtime,
                        rank_a,
                        option
                    )
                )
            


def main():
    slug_number = input('Введите номер: ')

    get_url_data(slug_number=slug_number)

if __name__ == '__main__':
    main()