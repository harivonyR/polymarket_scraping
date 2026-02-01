# -*- coding: utf-8 -*-
"""
Created on Sun Feb  1 19:36:52 2026

@author: Lenovo
"""

from script.piloterr import website_crawler
from script.polymarket import get_card_detail, get_cards
from bs4 import BeautifulSoup

news_url = "https://polymarket.com/new"
response = website_crawler(news_url)


soup = BeautifulSoup(response)
cards = get_cards(soup)

if cards :
    results = []
    
    for card in cards :
        card_detail = get_card_detail(card)
        results.append(card_detail)