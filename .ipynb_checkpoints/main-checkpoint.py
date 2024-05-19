# Initial commit to verify that git is working.
import requests
from bs4 import BeautifulSoup
import smtplib

import requests
from bs4 import BeautifulSoup

def scrape_website(url):
    """This function will scrape a website indicated by the input URL.

    This function will search for the website indicated by the ilnput URL and return the information from it.

    Parameters:
    param1 (string): Input URL. Currently, this function has no security for malicious incoming URLs.

    Returns:
    dataframe: Description of the return value

    Raises:
        ExceptionName: 'Invalid URL'.

    Examples:
        url = 'https://www.worldometers.info/world-population/'
        >>> function_name(url)
    result
    """

    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        # Extract specific data required
        titles = [title.text for title in soup.findall('h1')]
        return titles
    else:
        raise Exception('Invalid URL')

def monitor_website(url, condition_function):
    data = scrape_website()
    if data:
        return condition_function(data)
    return False

def sample_condition(data):
    # Check if specific title is present
    return "Current World Population" in data
