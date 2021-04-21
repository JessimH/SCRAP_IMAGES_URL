import requests
from bs4 import BeautifulSoup
from tqdm import tqdm

url = ""
page = requests.get(url)
souped = BeautifulSoup(page.content, "html.parser")
imgs = souped.find_all("img")
imgs = imgs[3:-1]

for img in tqdm(imgs):
    imgLink = img.attrs.get("src")
    image = requests.get(imgLink).content
    filename = r"scraping" + imgLink[imgLink.rfind("/"):]
    with open(filename, "wb") as file:
        file.write(image)
