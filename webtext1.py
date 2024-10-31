import requests
from bs4 import BeautifulSoup

class TextExtractor:
    def __init__(self, urls_file):
        self.urls_file = urls_file
    def get_html(self, url):
        try:
            response = requests.get(url)
            response.raise_for_status()
            return response.text
        except requests.RequestException:
            print("error")
            return None
    def extract_text(self):
        with open(self.urls_file, 'r') as file:
            urls = file.readlines()
        for i, url in enumerate(urls):
            url =url.strip()
            html = self.get_html(url)
            if html:
                soup = BeautifulSoup(html, 'html.parser')
                text = soup.get_text(separator="\n").strip()
                with open(str(i) + ".txt", 'w', encoding='utf-8') as output_file:
                    output_file.write(text)
                    print("текст з " + url + " збережено у " + str(i) + ".txt")

extractor = TextExtractor('c://lab14//webpages.txt')
extractor.extract_text()
