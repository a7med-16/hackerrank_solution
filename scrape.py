import requests
import os
from bs4 import BeautifulSoup

USERNAME = os.getenv("HR_USERNAME")

def fetch_solutions():
    url = f"https://www.hackerrank.com/rest/hackers/{USERNAME}/recent_challenges?offset=0&limit=50"
    r = requests.get(url)
    data = r.json()['models']

    if not os.path.exists("solutions"):
        os.makedirs("solutions")

    for item in data:
        title = item["name"].replace(" ", "_")
        slug = item["slug"]
        code_url = f"https://www.hackerrank.com/rest/contests/master/challenges/{slug}/download_solution"
        sol = requests.get(code_url).text

        with open(f"solutions/{title}.txt", "w", encoding="utf-8") as f:
            f.write(sol)

if _name_ == "_main_":
    fetch_solutions()
