#!/usr/bin/env python
# -*- coding: utf-8 -*-

from bs4 import BeautifulSoup
import urllib


def crawl():
    category_links = []
    products = []
    r = urllib.urlopen('http://epocacosmeticos.com.br').read()
    soup = BeautifulSoup(r, "html.parser")
    # TO NOT GET 'MARCAS' ENTRY
    menus =  soup.find_all("h2", class_="item_menu")
    for menu in menus:
        # TO NOT GET 'PROMOS' ENTRY
        sub = menu.find("ul", class_="sub")
        if sub:
            category_links.append(menu.a["href"])

    for category_link in category_links:
        r = urllib.urlopen(category_link).read()
        soup = BeautifulSoup(r, "html.parser")
        main = soup.find("div", class_="main").find("div", class_="n4colunas")
        product_list = main.find_all(lambda tag: tag.name == 'li' and 'helperComplement' not in tag['class'])

        for product_item in product_list:
            product_anchor = product_item.find("h3").a
            product_name = product_anchor.get_text().split('-')[0]
            product = {}
            product['name'] = product_name.strip().encode('utf8')
            product['url'] = product_anchor['href']
            price = product_item.find(class_='newPrice').get_text().split(" ")[1]
            product['price'] = price
            found = 0
            for p in products:
                if product['name'] == p['name']:
                    found = 0
                    break
            if found > 0:
                found = 0
                next
            products.append(product)
    # print(products)
    file = open('products.csv', 'w')
    file.write("name,price,url\n")
    for product in products:
        file.write(product['name'])
        file.write(',')
        file.write(product['price'])
        file.write(',')
        file.write(product['url'])
        file.write("\n")
    file.close()
            # product['name'] = product_item.find('h2').a.get_text()
crawl()
