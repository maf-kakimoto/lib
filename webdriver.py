# -*- coding: utf-8 -*-

from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def _webdriver(headless):

    options = Options()
    if headless:
        options.add_argument('--headless')
    DRIVER_PATH = ''
    driver = webdriver.Chrome(executable_path=DRIVER_PATH, options=options)

    return driver
