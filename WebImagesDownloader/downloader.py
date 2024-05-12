import requests
from bs4 import BeautifulSoup
from pathSage import pathSage
import tools

class Downloader:
    def __init__(self):
        self.ps = pathSage.pathSage()
        self.tool = tools.Tools()

    def download_one_img(self, url, img_ne, save_p, verify=True):
        try:
            img_data = requests.get(url).content # web url request launched
        except Exception:
            print("URL not found.")
            return
        
        img_pne = f"{save_p}{img_ne}"

        with open(img_pne, "wb") as file:
            print(f"\n> Get: {url}\n  Save to: {img_pne}")
            file.write(img_data) # download the image using the link 

        return (
            self.tool.is_corrupted_image(img_pne)
            if verify
            else True
        )

    def download_all_img(self, url, save_p):
        img_list = []
        r = requests.get(url) # web url request launched
        soup = BeautifulSoup(r.text, 'html.parser') # return html script
        images = soup.find_all('img') # fin all terms in the html script (default : img)
        print(images)

        print("Start finding and downloading...")
        for image in images:
            img_url = image['src']
            img_ne = img_url.rsplit('/', 1)[1]

            self.download_one_img(img_url, img_ne, save_p)

        return img_list