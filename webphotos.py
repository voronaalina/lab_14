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
    if not img_url.startswith("http"):
        img_url = url + img_url
        img_data = requests.get(img_url).content
    with open("images/image_" + str(i) + ".jpg", 'wb') as img_file:
        img_file.write(img_data)
    print("збережено" + "images/image_" +str(i) + ".jpg")
    