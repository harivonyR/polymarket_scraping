# -*- coding: utf-8 -*-
"""
Created on Sun Feb  1 19:36:52 2026

@author: Lenovo
"""

from script.polymarket_category import get_top_events_by_category
from script.polymarket_event import extract_event_detail


if __name__ == "__main__" :
    
    polymarket_culture = "https://polymarket.com/culture"
    acquired_companies_before_2027 = "https://polymarket.com/event/which-companies-will-be-acquired-before-2027"
    
    top_culture_event = get_top_events_by_category(polymarket_culture)
    event_detail = extract_event_detail(acquired_companies_before_2027)