# -*- coding: utf-8 -*-

from script.piloterr import website_crawler, website_rendering
from utils.selector import find_with_all_classes, find_with_classes
from bs4 import BeautifulSoup


def get_cards(url):
    response = website_crawler(url)
    
    soup = BeautifulSoup(response)
    classes = ["transition", "justify-between", "rounded-md", "shadow-md"]
    cards = find_with_all_classes(soup,classes)
    
    return cards

def get_detail(card):
    # get title
    data = {}
    title_classes = ["text-sm", "font-semibold", "w-fit", "line-clamp-3", "text-pretty"]
    title = find_with_classes(card,title_classes)
    
    data["title"] = title.text
    
    return data
    

if __name__ == "__main__" :
    culture_url = "https://polymarket.com/pop-culture"
    response = website_crawler(culture_url)
    
    #response = website_rendering(culture_url, wait_in_seconds=5, scroll=3)    # forbiden
    
    soup = BeautifulSoup(response)
    classes = ["transition", "justify-between", "rounded-md", "shadow-md"]
    cards = find_with_all_classes(soup,classes )
    
    res = []
    
    for card in cards :
        data = {}
        # get title
        title_classes = ["text-sm", "font-semibold", "w-fit", "line-clamp-3", "text-pretty"]
        title = find_with_classes(card,title_classes)
        
        data["title"] = title.text
        
        res.append(data)
        