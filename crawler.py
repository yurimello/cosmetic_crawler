#!/usr/bin/env python

from bs4 import BeautifulSoup
import urllib
r = urllib.urlopen('http://epocacosmeticos.com.br').read()
soup = BeautifulSoup(r, "html.parser")
print(soup)
