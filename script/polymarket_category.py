# -*- coding: utf-8 -*-

from script.piloterr import website_crawler, website_rendering
from utils.selector import find_with_all_classes, find_with_classes
from bs4 import BeautifulSoup


def get_cards(soup):
    """
    return card found in a soup (html response soup)
    """
    classes = ["transition", "justify-between", "rounded-md", "shadow-md"]
    cards = find_with_all_classes(soup,classes)
    
    if cards : return cards
    else : return []

def get_title(card):
    """
    input : 
        card : a beautifull soup object of a polymarket card on item list
    
    output :
        title : a string representing the title of the card
    """
    title_classes = ["text-sm", "font-semibold", "w-fit", "line-clamp-3", "text-pretty"]
    title = find_with_classes(card,title_classes)
    
    if title : return title.text
    else : return ""
    
def get_link(card):
    """
    Return absolute or relative link of the card.
    """
    a_tag = card.find("a", href=True)
    if not a_tag:
        return ""
    return "https://polymarket.com"+a_tag["href"]

 
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
    
    if volume : return volume.text
    else : return ""
    

def get_prop_title(prop):
    """
    return prop title
    """
    prop_title_classes = ["flex", "flex-1", "gap-2", "items-center", "min-w-0", "group", "cursor-pointer"]
    prop_title = find_with_classes(prop,prop_title_classes)
    
    if prop_title : return prop_title.text
    else : ""

def get_prop_chances(prop): 
    """
    return prop title
    """
    prop_chances_classes = ["font-semibold", "text-text-primary", "mr-1"]
    prop_chances = find_with_classes(prop,prop_chances_classes)
    
    if prop_chances : return prop_chances.text
    else : ""

def get_yes_no_chances(prop):
    """
    return yes oe no chances in an array
    """
    btns = prop.select("button")
    
    if btns :
        choices = []
        for btn in btns :
            a = [e.text for e in btn.select("span")]
            choices.append(a)
        return choices
    
    else : 
        return []

def get_gauge_details(card):
    gauge_classes = ["flex", "flex-col", "items-center", "w-full" ,"-translate-y-[30px]"]
    gauge = find_with_classes(card,gauge_classes)
    
    if gauge : return gauge.text
    else : return ""

def get_props_details(card):
    """
    return prop soup list in a card
    """
    props_classes = ["flex", "justify-between", "items-center", "gap-4", "w-full", "h-fit", "shrink-0"]
    props = find_with_all_classes(card,props_classes)
    
    if props :
        props_detail = []
        for prop in props :
            #prop = props[0]
            data = {}
            data["prop_title"] = get_prop_title(prop)
            data["prop_chances"] = get_prop_chances(prop)
            data["yes_no_chances"] = get_yes_no_chances(prop)
            
            props_detail.append(data)
            
        return props_detail
    else : return []

def get_card_detail(card):
    data = {}
    
    data["title"] = get_title(card)
    data["volume"] = get_volume(card)
    data["props_detail"] = get_props_details(card)
    data["gauge_detail"] = get_gauge_details(card)
    data["link"] = get_link(card)
    
    return data

def scrape_categories_event(section_url):
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

if __name__ == "__main__" :
    pop_culture_url = "https://polymarket.com/pop-culture"
    results = scrape_categories_event(pop_culture_url)
    
    
