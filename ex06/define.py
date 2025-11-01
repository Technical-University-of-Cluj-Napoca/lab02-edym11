import sys
import requests
from bs4 import BeautifulSoup

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Invalid arguments entered!")
    word = sys.argv[1]
    site = "https://www.oxfordlearnersdictionaries.com/definition/english/"
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}
    response = requests.get(site+word, headers=headers)
    soup = BeautifulSoup(response.text, "html.parser")
    defs = soup.find_all("span", class_ = "def")
    results = []
    for d in defs:
        text = d.text.strip()
        results.append(text)
    if results:
        print(results[0])