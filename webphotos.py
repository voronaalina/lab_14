import requests
from bs4 import BeautifulSoup
import os

url = 'https://www.bbc.com/culture/article/20241018-how-monets-paintings-changed-the-way-we-see-london'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')
os.makedirs("images", exist_ok=True)
images = soup.find_all('img')
for i, img in enumerate(images):
    img_url = img.get('src')
    if img_url:
        if not img_url.startswith("http"):
            img_url = 'https://www.bbc.com' + img_url  
        try:
            img_data = requests.get(img_url).content
            with open("c:\\lab14\\" + "images/image_" + str(i) +".jpg", 'wb') as img_file:
                img_file.write(img_data)
            print("збережено " + "images/image_" + str(i) + ".jpg")
        except requests.RequestException:
            print("Помилка")