# -*- coding: utf-8 -*-
"""
Created on Sun Feb  1 19:36:52 2026

@author: Lenovo
"""

from script.piloterr import website_crawler
from script.polymarket_category import get_card_detail, get_cards
from bs4 import BeautifulSoup

polymarket_tech = "https://polymarket.com/tech"
polymarket_world = "https://polymarket.com/world"
acquired_companies_before_2027 = "https://polymarket.com/event/which-companies-will-be-acquired-before-2027"

def scrape_category_events(section_url):
    """
    Take a category url as input and return top events
    
    """
    response = website_crawler(section_url)

    soup = BeautifulSoup(response)
    cards = get_cards(soup)

    if cards :
        results = []
    
        for card in cards :
            card_detail = get_card_detail(card)
            results.append(card_detail)
            
    return results

def scrape_event_detail(event_url):
    pass


if __name__ == "__main__" :
    top_tech_event = scrape_category_events(polymarket_tech)