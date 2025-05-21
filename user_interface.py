import csv

history = []

def save_history_to_csv(filename="history.csv"):
    with open(filename, mode='w', newline='', encoding='utf-8') as file:
        fieldnames = ['title', 'link', 'category']
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(history)


def load_history_from_csv(filename="history.csv"):
    global history
    try:
        with open(filename, mode='r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            history = [row for row in reader]
    except FileNotFoundError:
        history = []


def load_news_by_category(filename, chosen_category):
    try:
        with open(filename, mode='r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            return [row for row in reader if row['category'].lower() == chosen_category.lower()]
    except FileNotFoundError:
        print("CSV fails nav atrasts.")
        return []


def show_news(news_list):
    if not news_list:
        print("Ziņas nav atrastas.")
        return

    for idx, article in enumerate(news_list):
        print(f"\n{idx + 1}. {article['title']}")
        print(f"Saite: {article['link']}")
        history.append(article)

    save_history_to_csv()


def show_history():
    print("\n --- Ziņu vēsture ---")
    if not history:
        print("Nav skatīto ziņu.")
        return
    for article in reversed(history[-5:]):
        print(f"- {article['title']} ({article['link']})")
