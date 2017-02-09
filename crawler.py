#!/usr/bin/env python

from bs4 import BeautifulSoup
import urllib

def crawl():
    r = urllib.urlopen('http://epocacosmeticos.com.br').read()
    soup = BeautifulSoup(r, "html.parser")
    # TO NOT GET 'MARCAS' ENTRY
    menus =  soup.find_all("h2", class_="item_menu")
    for menu in menus:
        # TO NOT GET 'PROMOS' ENTRY
        sub = menu.find("ul", class_="sub")
        if sub:
            print(menu.a["href"])

crawl()
