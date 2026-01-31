# -*- coding: utf-8 -*-

import requests
from credential import x_api_key
from utils.helper import save_html_to_file

def website_crawler(site_url):
    url = "https://piloterr.com/api/v2/website/crawler"
    
    headers = {"x-api-key": x_api_key}
    querystring = {"query":site_url}
    
    response = requests.request("GET", url, headers=headers,params=querystring)
    
    clean_html = response.text.encode('utf-8').decode('unicode_escape')
    clean_html = clean_html.encode('latin-1').decode('utf-8')
   
    return clean_html

if __name__ == "__main__" :
    polymrket_home = "https://polymarket.com/"
    response = website_crawler(polymrket_home)
    
    save_html_to_file(response, "output/index.html")
