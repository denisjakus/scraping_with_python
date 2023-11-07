import sys
import re
from bs4 import BeautifulSoup
import requests


def is_valid_url(url):
    regex = r"(?i)\b((?:https?://|www\d{0,3}[.]|[a-z0-9.\-]+[.][a-z]{2,4}/)(?:[^\s()<>]+|\(([^\s()<>]+|(\([^\s()<>]+\)))*\))+(?:\(([^\s()<>]+|(\([^\s()<>]+\)))*\)|[^\s`!()\[\]{};:'\".,<>?«»“”‘’]))"

    is_match = re.fullmatch(regex, url)

    if is_match == None:
        return False 
    else:
        return True

def scrape_url(url):
    # print(f'URL: {url} is valid!')
    res = requests.api.get(url)
    html_parser = BeautifulSoup(res.text, 'html.parser')
    print('OUTPUT:\n')
    titles = html_parser.select('.titleline')
    points = html_parser.select('.score')
    print(points[0])
    t = create_custom_hacker_news(titles,points)
    # print(res.text)
    return

def create_custom_hacker_news(links,votes):
    hn = []

    for index, item in enumerate(links):
        title = links[index].getText()
        href = links[index].find_all('a')[0].get('href')
        hn.append({'title': title, 'href': href})

    return hn


if __name__ == "__main__":
   
    url_to_scrape = sys.argv[1] 

    is_valid = is_valid_url(url_to_scrape)

    if is_valid:
         scrape_url(url_to_scrape)
    else:
        print("Given url is NOT valid!")
    
    sys.exit()
