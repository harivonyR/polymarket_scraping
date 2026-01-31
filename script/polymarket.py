# -*- coding: utf-8 -*-

from script.piloterr import website_crawler, website_rendering
from utils.selector import find_with_all_classes, find_with_classes
from bs4 import BeautifulSoup


def get_cards(response_soup):

    classes = ["transition", "justify-between", "rounded-md", "shadow-md"]
    cards = find_with_all_classes(soup,classes)
    
    return cards

def get_title(card):
    """
    input : 
        card : a beautifull soup object of a polymarket card on item list
    
    output :
        title : a string representing the title of the card
    """
    title_classes = ["text-sm", "font-semibold", "w-fit", "line-clamp-3", "text-pretty"]
    title = find_with_classes(card,title_classes)
    
    return title.text
    

def get_volume(card):
    """
    input : 
        card : a beautifull soup object of a polymarket card on item list
    
    output :
        title : a string representing the volume placed in an item (can be a text e.g. : new)
    """
    # get the card footer
    card_footer_classes = ["flex", "gap-2", "justify-between", "items-center", "w-full", "overflow-x-auto", "whitespace-nowrap"]
    card_footer = find_with_classes(card, card_footer_classes)
    
    
    # get volume
    volume_classes = ["flex", "items-center", "gap-1"]
    volume = find_with_classes(card_footer, volume_classes)
    
    return volume.text
    


if __name__ == "__main__" :
    culture_url = "https://polymarket.com/pop-culture"
    response = website_crawler(culture_url)
    
    #response = website_rendering(culture_url, wait_in_seconds=5, scroll=3)    # forbiden
    
    soup = BeautifulSoup(response)
    cards = get_cards(soup)
    
    res = []
    
    for card in cards :
        data = {}
        
        data["title"] = get_title(card)
        data["volume"] = get_volume(card)
        
        res.append(data)
        