import os
import requests
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("MY_NEWS_KEY")

url = f"https://newsapi.org/v2/top-headlines?category=technology&apiKey={api_key}"

def fetch_news():
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        news = data['articles'] 
    
        with open("news_log.txt", "w", encoding="utf-8") as file:
            file.write("--- today's latest news ---\n\n")
            
            for item in news:
                title = item['title']
                description = item['description']
                
                print(f"Heading: {title}\n")
                
                file.write(f"Title: {title}\nDetail: {description}\n")
                file.write("-" * 30 + "\n")
        
        print("all news saved in news_log.txt.")
    else:
        print("I couldnt find data there may be api issue.")

fetch_news()