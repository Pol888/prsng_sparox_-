import requests
from bs4 import BeautifulSoup
from selenium import webdriver
import time
import csv

def work(url):
    global manufacturer
    headers = {'Accept': '*/*',
               'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64;'
                             ' x64) AppleWebKit/537.36 '
                             '(KHTML, like Gecko) Chrome/104.0.5112.124 '
                             'YaBrowser/22.9.3.888 Yowser/2.5 Safari/537.36'
               }
    # driver = webdriver.Chrome()
    # driver.get(url)
    # time.sleep(4)
    #
    # soup = BeautifulSoup(driver.page_source, 'lxml')
    # menu = soup.find('div', class_="menu menu-brands")
    a = ['КамАЗ', 'МАЗ', 'Газ', 'УралАЗ', 'Краз', 'Масло', 'Инструмент', 'Электрика']
    # spisokL = []
    # for i in menu:
    #    for j in a:
    #        if j.lower() in str(i).lower():
    #            lnk = i.find('a').get('href')
    #            spisokL.append(lnk + '\n')
    #
    # with open('link888.txt', 'w', encoding='utf-8') as file:
    #    file.writelines(spisokL[1:])
    # driver.close()

    with open('vot_on.csv', 'a', encoding='utf-8', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Раздел', 'Ссылка на раздел', 'Имя категории', 'Ссылка на категорию', 'Ссылка на изображение',
                         'Название продукта', 'Ссылка на изображение продукта', 'Артикуль', 'Код', 'Производитель',
                         'Доступность', 'Цена'])
    with open('link888.txt', 'r', encoding='utf-8') as file:
        file = file.readlines()

    for num, i in enumerate(file):  # +++++++++++++++++++++++++++++++++++++++++++ start ++++++++++++++++++++++++++++
        i = i.replace('\n', '')
        r = requests.get(url + i, headers=headers)
        soup = BeautifulSoup(r.text, 'lxml')
        category = soup.find_all('div', class_="alphabet-list-item")
        for j in category:
            category_link = j.find('a', class_="alphabet-list-link").get('href')
            picture_link = j.find('img', class_="alphabet-logo").get('src')
            category_name = j.find('span', class_="tag-link").text
            r = requests.get(url + category_link, headers=headers)
            soup = BeautifulSoup(r.text, 'lxml')
            product_card = soup.find_all('div', class_="ibox-content hidden-xs hidden-sm p-xs")
            for l in product_card:
                try:
                    picture_img_link = l.find('img').get('src')
                    prod_name = l.find('span').text
                    artikul = l.find(class_="m-b-xs text-warning").text.split(':')[1]
                    cod = l.find(class_="small m-b-none").text.split(':')[1]
                    if len(l.find_all('p', class_="small m-b-none")) > 1:
                        manufacturer = l.find_all('p', class_="small m-b-none")[1].text.split(':')[1].strip()
                    availability = l.find(class_="col-md-2 col-lg-2").find('h3').text.strip()
                    price = l.find('h3', class_="text-warning").text
                    with open('vot_on.csv', 'a', encoding='utf-8', newline='') as file:
                        writer = csv.writer(file)
                        writer.writerow(
                            [a[num], i, category_name, category_link, picture_link, prod_name, picture_img_link,
                             artikul, cod, manufacturer, availability, price])
                        print(a[num], i, category_name, category_link, picture_link, prod_name, picture_img_link,
                              artikul, cod, manufacturer, availability, price)
                except:
                    print('Error')

    # l = soup.find(class_="alphabet-list-item")
    # print(l)
    # menu = soup.find_all('div', class_="kamaz")
    # for i in menu:    #    print(i)

    #    a = ['КамАЗ', 'МАЗ', 'Газ', 'УралАЗ', 'Краз', 'Масло', 'Инструмент', 'Электрика']
    #    spisikL = []
    #    for i in menu:
    #        for j in a:


#
#            if j.lower() in str(i).lower():
#                lnk = i.find('a').get('href')
#                spisikL.append(lnk + '\n')
# with open('link.txt', 'w', encoding='utf-8') as file:
#    file.writelines(spisikL[1:])


# driver.close()


def main():
    url = 'https://sparox.ru'
    'https://sparox.ru/catalog/kamaz'
    work(url)


if __name__ == '__main__':
    main()