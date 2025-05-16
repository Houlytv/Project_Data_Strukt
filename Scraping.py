import requests
from bs4 import BeautifulSoup
import csv

def scrape_news(category):
    url = f"https://www.tvnet.lv/{category}"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    articles = []
    for item in soup.select('article'):
        title_tag = item.find('h3') or item.find('h2')
        if title_tag:
            title = title_tag.text.strip()
            link = item.find('a')['href']
            articles.append({
                'title': title,
                'link': link,
                'category': category
            })
    return articles

def save_to_csv(news_list, filename="news.csv"):
    with open(filename, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=['title', 'link', 'category'])
        writer.writeheader()
        writer.writerows(news_list)
