# -*- coding: utf-8 -*-

import requests
from credential import x_api_key
from utils.helper import save_html_to_file

def website_crawler(site_url):
    """
    """
    url = "https://piloterr.com/api/v2/website/crawler"
    
    headers = {"x-api-key": x_api_key}
    querystring = {"query":site_url}
    
    response = requests.request("GET", url, headers=headers,params=querystring)
    
    clean_html = response.text.encode('utf-8').decode('unicode_escape')
    clean_html = clean_html.encode('latin-1').decode('utf-8')
   
    return clean_html

def website_rendering(site_url, wait_in_seconds=5, scroll=3):
    """
    Render a website using Piloterr API.
    Supports optional scroll to bottom.
    """
    url = "https://piloterr.com/api/v2/website/rendering"
    querystring = {"query": site_url, "wait_in_seconds": str(wait_in_seconds)}
    headers = {"x-api-key": x_api_key}  # Assure-toi que x_api_key est défini globalement

    # we don't need to scroll
    if scroll == 0:
        response = requests.get(url, headers=headers, params=querystring)
    
    # with scrolling
    else:
        
        smooth_scroll = [
            {
                "type": "scroll",
                "x": 0,
                "y": 200,         # scrolling height : 2000 pixels down
                "duration": 3,     # scrolling duration
                "wait_time_s": 4   # wait time in second (s) before the next instruction
            }
        ]

        instruction = {
            "query": site_url,
            "wait_in_seconds": str(wait_in_seconds),
            "browser_instructions": smooth_scroll*scroll
        }

        response = requests.post(url, headers=headers, json=instruction)
    
    # decode double escape "\\" and inline "\n" 
    clean_html = response.text.encode('utf-8').decode('unicode_escape')
    
    # decode special character 
    clean_html = clean_html.encode('latin-1').decode('utf-8')
    
    return clean_html

if __name__ == "__main__" :
    polymrket_home = "https://polymarket.com/"
    elon_tweet = "https://polymarket.com/event/elon-musk-of-tweets-january-13-january-20"
    response = website_crawler(elon_tweet)
    
    save_html_to_file(response, "output/index.html")


    url = "https://clob.polymarket.com/price"
    
    response = requests.get(url)
    
    print(response.text)