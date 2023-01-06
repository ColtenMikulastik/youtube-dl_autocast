
import requests
from bs4 import BeautifulSoup

# set the headers that I think that youtube music wants
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}


page = requests.get("https://music.youtube.com/playlist?list=OLAK5uy_nsWnfuCuabdw_jqiV6vht2Js1r4u8GbvQ", headers=headers)
soup = BeautifulSoup(page.content, 'html.parser')

stringsoup = str(soup)

stringsoup = stringsoup[stringsoup.find("thumbnails"):]

stringsoup = stringsoup[stringsoup.find("https"):]

sub_stringsoup = stringsoup[: stringsoup.find("\\x")]

sub_stringsoup = sub_stringsoup.replace("\\/","/")
print(sub_stringsoup)

image_req = requests.get(sub_stringsoup)

with open("thumbnail.jpg", "wb") as file:
    file.write(image_req.content)
