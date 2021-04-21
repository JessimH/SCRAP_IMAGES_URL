# requests allows us to play with Urls
import requests

# BeautifulSoup is a webscraping module
from bs4 import BeautifulSoup

# Tqdm just show a progressbar in order to see when the loop ends.
from tqdm import tqdm

print('✨Enter an url with beautiful images✨:')
url = input()
page = requests.get(url)
souped = BeautifulSoup(page.content, "html.parser")
img_arr = souped.find_all("img")
img_arr = img_arr[3:-1]

for img in tqdm(img_arr):
    imgSrc = img.attrs.get("src")
    image = requests.get(imgSrc).content
    filename = r"scraping" + imgSrc[imgSrc.rfind("/"):]
    with open(filename, "wb") as file:
        file.write(image)
print('Tadaaa ! you can see your images in the "scraping" folder ! 🔥')
