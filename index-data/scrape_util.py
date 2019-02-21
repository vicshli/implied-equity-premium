from bs4 import BeautifulSoup
from selenium import webdriver
from urllib import request as re
import csv


def soup_maker(url, headless=False):
    """Returns a BeautifulSoup, given an url."""
    content = re.urlopen(url).read()
    soup = BeautifulSoup(content, 'html.parser')
    return soup


def soup_maker_webdriver(url, headless=False):
    """Return a BeaultifulSoup object, given a url.
    This version utilizes selenium driver.
    """
    try: 
        with webdriver.Chrome('_driver/chromedriver') as driver:
            driver.get(url)
            soup = BeautifulSoup(driver.page_source, 'html.parser')
        return soup
    except:
        return None


def dict_to_csv(dict, filename):
    """Write a dictionary to a new csv file, given a dict and a filename.
    Note that if a file named `filename` already exists, this function 
    will override that file without warning. 
    """
    keys = dict.keys()
    with open(filename, 'w', newline='') as output_file:
        dict_writer = csv.DictWriter(output_file, keys)
        dict_writer.writeheader()
        dict_writer.writerow(dict)
