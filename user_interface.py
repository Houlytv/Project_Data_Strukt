import csv

history = []

def load_news(filename, chosen_category): 
    try:
        with open(filename, mode='r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            return [row for row in reader if row['category'].lower() == chosen_category.lower()]
    except FileNotFoundError:
        print("csv fails nav atrasts.")
        return []

def show_news(news_list):
    if not news_list:
        print("ziņas nav atrastas.")
        return

    for idx, article in enumerate(news_list):
        print(f"\n{idx+1}. {article['title']}")
        print(f"saite: {article['https://www.tvnet.lv/']}")
        print(f"datums: {article.get('date', 'nav pieejams')}")
        history.append(article)