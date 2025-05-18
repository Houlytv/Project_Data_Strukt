from Data_strukt import scrape_news, save_to_csv
from Web_scraping import load_news_by_category, show_news, show_history, save_history_to_csv, load_history_from_csv

def main():
    load_history_from_csv()
    category = input("Ievadi tēmu (piem. sports, politika): ").strip()

    # 1. Nolasām jaunumus
    news = scrape_news(category)
    if not news:
        print("Neizdevās atrast nevienu rakstu.")
        return
    save_to_csv(news)

    # 2. Lietotāja interfeiss
    filtered_news = load_news_by_category("news.csv", category)
    show_news(filtered_news)
    save_history_to_csv()
    # 3. Parādīt vēsturi
    choice = input("Rādīt pēdējās ziņas? (j/n): ")
    if choice.lower() == 'j':
        show_history()


if __name__ == "__main__":
    main()
