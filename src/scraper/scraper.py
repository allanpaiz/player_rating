import requests
from bs4 import BeautifulSoup


# TODO: Make work

def fetch_page(url):
    response = requests.get(url)
    if response.status_code == 200:
        return response.text
    else:
        print(f"Failed to fetch {url} with status code {response.status_code}")
        return None

def parse_html(html_content):
    return BeautifulSoup(html_content, "html.parser")

def extract_team_links(soup):
    team_links = []
    for link in soup.select(".teams a"):
        team_links.append(link["href"])
    return team_links
