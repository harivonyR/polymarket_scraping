# -*- coding: utf-8 -*-

from script.piloterr import website_crawler, website_rendering
from utils.selector import find_with_all_classes, find_with_classes
from bs4 import BeautifulSoup


def get_event_title(event):
    title_classes = ["!font-semibold", "!text-2xl", "text-pretty"]
    title = find_with_classes(event,title_classes)
    
    if title : return title.text
    else : return ""
    
 
def get_event_volume(event):
    # get the card footer
    volume_classes = ["text-text-primary", "text-[13px]", "font-medium", "whitespace-nowrap"]
    volume = find_with_classes(event, volume_classes)
    
    if volume : return volume.text
    else : return ""
    
def get_event_category(event):
    categories_classes = ["flex", "items-center", "gap-1"]
    categories = find_with_classes(event, categories_classes)
    
    if categories : return categories.text.split("·")
    else : return []

def get_event_end(event):
    event_end_classes = ["text-[13px]", "text-text-secondary", "gap-1.5", "whitespace-nowrap", "flex", "items-center", "md:mr-1"]
    
    event_end = find_with_classes(event, event_end_classes)
    
    if event_end : return event_end.text
    else : return ""

def get_prop_title(prop):
    """
    return prop title
    """
    prop_title_classes = ["overflow-hidden", "text-ellipsis", "whitespace-nowrap", "max-w-[280px]", "my-auto"]
    prop_title = find_with_classes(prop,prop_title_classes)
    
    if prop_title : return prop_title.text
    else : ""

def get_prop_chances(prop): 
    """
    return prop title
    """
    prop_chances_classes = ["font-medium", "text-[28px]", "text-text-primary"]
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

def get_prop_volume(prop):
    prop_volume_classes = ["text-xs", "text-text-secondary", "whitespace-nowrap"]
    prop_volume = find_with_classes(prop,prop_volume_classes)
    
    if prop_volume : return prop_volume.text
    else : ""
    

def get_props_details(card):
    """
    return prop soup list in a card
    """
    props_classes = ["w-full", "flex", "flex-row", "justify-between", "min-h-12", "z-1"]
    props = find_with_all_classes(card,props_classes)
    
    if props :
        props_detail = []
        for prop in props :
            #prop = props[0]
            data = {}
            data["prop_title"] = get_prop_title(prop)
            data["prop_chances"] = get_prop_chances(prop)
            data["yes_no_chances"] = get_yes_no_chances(prop)
            data["prop_volume"] = get_prop_volume(prop)
            
            props_detail.append(data)
            
        return props_detail
    else : return []

def get_event_detail(event):
    data = {}
    
    data["title"] = get_event_title(event)
    data["volume"] = get_event_volume(event)
    data["event_end"] = get_event_end(event)
    data["categories"] = get_event_category(event)
    data["proposition"] = get_props_details(event)
    
    return data


if __name__ == "__main__" :
    acquired_companies_before_2027= "https://polymarket.com/event/which-companies-will-be-acquired-before-2027"
    response = website_crawler(acquired_companies_before_2027)
    
    event_soup = BeautifulSoup(response)
    
    event_detail = get_event_detail(event_soup)