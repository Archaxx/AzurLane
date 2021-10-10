from urllib.request import urlopen, urlretrieve
from bs4 import BeautifulSoup

URL = "https://azurlane.koumakan.jp/List_of_Ships_by_Image"


def get_page_content():
    return urlopen(URL).read()


def parse(body):
    soup = BeautifulSoup(body, "html.parser")
    divs = soup.find_all("div", {"style": "display:flex; flex-flow:row wrap;"})
    titles = soup.find_all("span", {"class": "mw-headline"})
    titles_id = [title.attrs.get("id") for title in titles]
    create_folders()
    return [(f"{title}/{img.attrs.get('alt')}", f"https://azurlane.koumakan.jp/{img.attrs.get('src')}")
            for div, title in zip(divs, titles_id)
            for ship_div in div.children
            if ship_div.name == "div"
            for child in ship_div.children
            if (classes := child.attrs.get("class")) and "alc-img" in classes
            for a in child.children
            for img in a.children]


def create_folders():
    pass


def download_all_images(images_url_list):
    for filename, url in images_url_list:
        print(filename)
        urlretrieve(url, f"images/{filename}.jpg")


if __name__ == '__main__':
    images_list = parse(get_page_content())
    download_all_images(images_list)


