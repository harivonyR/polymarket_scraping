# -*- coding: utf-8 -*-

from script.piloterr import website_crawler
from utils.selector import find_with_all_classes, find_with_classes
from bs4 import BeautifulSoup


# ============================================================
# CSS SELECTORS (centralized for readability & maintenance)
# ============================================================

EVENT_TITLE_CLASSES = ["!font-semibold", "!text-2xl", "text-pretty"]
EVENT_VOLUME_CLASSES = ["text-text-primary", "text-[13px]", "font-medium", "whitespace-nowrap"]
EVENT_CATEGORY_CLASSES = ["flex", "items-center", "gap-1"]
EVENT_END_CLASSES = ["text-[13px]", "text-text-secondary", "gap-1.5", "whitespace-nowrap", "flex", "items-center", "md:mr-1"]

PROP_CONTAINER_CLASSES = ["w-full", "flex", "flex-row", "justify-between", "min-h-12", "z-1"]
PROP_TITLE_CLASSES = ["overflow-hidden", "text-ellipsis", "whitespace-nowrap", "max-w-[280px]", "my-auto"]
PROP_CHANCES_CLASSES = ["font-medium", "text-[28px]", "text-text-primary"]
PROP_VOLUME_CLASSES = ["text-xs", "text-text-secondary", "whitespace-nowrap"]


# ============================================================
# EVENT LEVEL EXTRACTION
# ============================================================

def get_event_title(event):
    title = find_with_classes(event, EVENT_TITLE_CLASSES)
    return title.text if title else ""


def get_event_volume(event):
    volume = find_with_classes(event, EVENT_VOLUME_CLASSES)
    return volume.text if volume else ""


def get_event_category(event):
    categories = find_with_classes(event, EVENT_CATEGORY_CLASSES)
    return categories.text.split("·") if categories else []


def get_event_end(event):
    event_end = find_with_classes(event, EVENT_END_CLASSES)
    return event_end.text if event_end else ""


# ============================================================
# PROPOSITION (MARKET) LEVEL EXTRACTION
# ============================================================

def get_prop_title(prop):
    title = find_with_classes(prop, PROP_TITLE_CLASSES)
    return title.text if title else ""


def get_prop_chances(prop):
    chances = find_with_classes(prop, PROP_CHANCES_CLASSES)
    return chances.text if chances else ""


def get_prop_volume(prop):
    volume = find_with_classes(prop, PROP_VOLUME_CLASSES)
    return volume.text if volume else ""


def get_yes_no_chances(prop):
    buttons = prop.select("button")
    if not buttons:
        return []

    choices = []
    for button in buttons:
        values = [span.text for span in button.select("span")]
        choices.append(values)

    return choices


def get_props_details(event):
    props = find_with_all_classes(event, PROP_CONTAINER_CLASSES)
    if not props:
        return []

    results = []

    for prop in props:
        results.append({
            "prop_title": get_prop_title(prop),
            "prop_chances": get_prop_chances(prop),
            "yes_no_chances": get_yes_no_chances(prop),
            "prop_volume": get_prop_volume(prop),
        })

    return results


# ============================================================
# PUBLIC API
# ============================================================

def extract_event_detail(event_url):
    response = website_crawler(event_url)
    soup = BeautifulSoup(response)

    return {
        "title": get_event_title(soup),
        "volume": get_event_volume(soup),
        "event_end": get_event_end(soup),
        "categories": get_event_category(soup),
        "proposition": get_props_details(soup),
    }


# ============================================================
# DEBUG / LOCAL TEST
# ============================================================

if __name__ == "__main__":
    event_url = "https://polymarket.com/event/which-companies-will-be-acquired-before-2027"
    event_detail = extract_event_detail(event_url)
