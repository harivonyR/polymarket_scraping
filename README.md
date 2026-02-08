# Polymarket Scraper (Tutorial Project)

This project demonstrates how to **scrape Polymarket category pages and individual events** using Piloterr API.

The goal is **educational**:
understand how to read the DOM of a modern website, identify relevant selectors, and extract visible information such as **popular events and volumes**, without relying on private APIs or complex abstractions.

This scraper focuses on:
- category pages (e.g. Tech, Culture, Geopolitics)
- individual event pages

---

## Use cases

Typical use cases for this project:

- Learn how to scrape a **React-based website**
- Practice **DOM inspection and selector reasoning**
- Extract:
  - top popular events from a category
  - detailed information from a specific event page
- Build datasets for:
  - data analysis
  - monitoring trends
  - educational scraping tutorials

⚠️ This project is **not production-ready** and is not intended for long-term automated scraping.

---

## Requirements
- Piloterr API key
- Python 3.9+
- beautifulsoup4
- requests

Install dependencies:

```bash
pip install BeautifulSoup requests
```

---

## Project structure

```
polymarket-scraper/
│
├── main.py
├── script/
│   ├── polymarket_category.py   # Scrape category pages
│   ├── polymarket_event.py      # Scrape individual event pages
│   └── piloterr.py              # HTML fetching logic
│
├── credential.py                # API key
└── README.md
```

---

## Usage

```python
from script.polymarket_category import get_top_events_by_category
from script.polymarket_event import extract_event_detail


if __name__ == "__main__":

    polymarket_culture = "https://polymarket.com/culture"
    acquired_companies_before_2027 = (
        "https://polymarket.com/event/which-companies-will-be-acquired-before-2027"
    )

    top_culture_event = get_top_events_by_category(polymarket_culture)
    event_detail = extract_event_detail(acquired_companies_before_2027)
```

---

## Notes & limitations

- Selectors rely on **visible DOM structure**
- Class names and inline styles may change
- Virtual scrolling can affect results

These constraints are intentional to keep the tutorial realistic.

---

## Disclaimer

This repository is provided for **educational purposes only**.
Always review Polymarket’s Terms of Service and applicable laws before scraping.
