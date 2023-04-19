
from src.scraper.scraper import fetch_page
# Figure out how to import functions from different folders
# 


url = "https://www.sports-reference.com/cbb/"


html_content = fetch_page(url)
# soup = parse_html(html_content)
# html_content = fetch_page(url)
# team_links = extract_team_links(soup)

print(html_content)