# -*- coding: utf-8 -*-

import requests
import time
from lib import headers
from bs4 import BeautifulSoup


def _soup(url):

    req_headers = headers._headers()
    site = requests.get(url, headers=req_headers)
    soup = BeautifulSoup(site.content, 'lxml')

    return soup


def _driver(url, driver):

    driver.get(url)
    time.sleep(5)
    html = driver.page_source.encode('utf-8')
    soup = BeautifulSoup(html, 'html.parser')

    return soup
