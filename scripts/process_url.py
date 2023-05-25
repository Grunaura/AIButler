'''
Author: Adam Messick
Date: 5/24/2023
This file contains the code to fetch content from a URL.
'''

import requests
from bs4 import BeautifulSoup

def fetch_url_content(url):
    '''
    Fetches the content of a given URL.

    Args:
        url (str): The URL to fetch.

    Returns:
        str: The raw content from the fetched URL.
    '''
    try:
        response = requests.get(url)
        response.raise_for_status()
    except requests.RequestException as e:
        print(f"Request to {url} failed: {e}")
        return None
    
    return response.text

def parse_url_content(content):
    '''
    Parses HTML content from a URL.

    Args:
        content (str): The HTML content to parse.

    Returns:
        str: The parsed text content from the HTML.
    '''
    soup = BeautifulSoup(content, 'html.parser')
    parsed_content = soup.get_text(separator='\n')

    return parsed_content
