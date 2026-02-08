# -*- coding: utf-8 -*-

from script.piloterr import website_crawler
from utils.selector import find_with_all_classes, find_with_classes
from bs4 import BeautifulSoup


# ============================================================
# CSS SELECTORS (centralized for tutorial readability)
# ============================================================

CARD_CLASSES = ["transition", "justify-between", "rounded-md", "shadow-md"]
CARD_TITLE_CLASSES = ["text-sm", "font-semibold", "w-fit", "line-clamp-3", "text-pretty"]
CARD_FOOTER_CLASSES = ["flex", "gap-2", "justify-between", "items-center", "w-full", "overflow-x-auto", "whitespace-nowrap"]
CARD_VOLUME_CLASSES = ["flex", "items-center", "gap-1"]

GAUGE_CLASSES = ["flex", "flex-col", "items-center", "w-full", "-translate-y-[30px]"]

PROP_CONTAINER_CLASSES = ["flex", "justify-between", "items-center", "gap-4", "w-full", "h-fit", "shrink-0"]
PROP_TITLE_CLASSES = ["flex", "flex-1", "gap-2", "items-center", "min-w-0", "group", "cursor-pointer"]
PROP_CHANCES_CLASSES = ["font-semibold", "text-text-primary", "mr-1"]


# ============================================================
# CARD LEVEL EXTRACTION
# ============================================================

def get_cards(soup):
    return find_with_all_classes(soup, CARD_CLASSES) or []


def get_title(card):
    title = find_with_classes(card, CARD_TITLE_CLASSES)
    return title.text if title else ""


def get_link(card):
    a_tag = card.find("a", href=True)
    return f"https://polymarket.com{a_tag['href']}" if a_tag else ""


def get_volume(card):
    footer = find_with_classes(card, CARD_FOOTER_CLASSES)
    if not footer:
        return ""

    volume = find_with_classes(footer, CARD_VOLUME_CLASSES)
    return volume.text if volume else ""


def get_gauge_details(card):
    gauge = find_with_classes(card, GAUGE_CLASSES)
    return gauge.text if gauge else ""


# ============================================================
# PROPOSITION LEVEL EXTRACTION
# ============================================================

def get_prop_title(prop):
    title = find_with_classes(prop, PROP_TITLE_CLASSES)
    return title.text if title else ""


def get_prop_chances(prop):
    chances = find_with_classes(prop, PROP_CHANCES_CLASSES)
    return chances.text if chances else ""


def get_yes_no_chances(prop):
    buttons = prop.select("button")
    if not buttons:
        return []

    return [
        [span.text for span in button.select("span")]
        for button in buttons
    ]


def get_props_details(card):
    props = find_with_all_classes(card, PROP_CONTAINER_CLASSES)
    if not props:
        return []

    results = []

    for prop in props:
        results.append({
            "prop_title": get_prop_title(prop),
            "prop_chances": get_prop_chances(prop),
            "yes_no_chances": get_yes_no_chances(prop),
        })

    return results


# ============================================================
# CARD AGGREGATION
# ============================================================

def get_card_detail(card):
    return {
        "title": get_title(card),
        "volume": get_volume(card),
        "props_detail": get_props_details(card),
        "gauge_detail": get_gauge_details(card),
        "link": get_link(card),
    }


# ============================================================
# PUBLIC API
# ============================================================

def get_top_events_by_category(category_url):
    response = website_crawler(category_url)
    soup = BeautifulSoup(response)

    cards = get_cards(soup)

    return [get_card_detail(card) for card in cards]


# ============================================================
# LOCAL TEST
# ============================================================

if __name__ == "__main__":
    pop_culture_url = "https://polymarket.com/pop-culture"
    event_list = get_top_events_by_category(pop_culture_url)
