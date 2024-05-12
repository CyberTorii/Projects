import requests
from bs4 import BeautifulSoup
import os
import re
from pathSage import pathSage
from PIL import Image

class Tools:
    def __init__(self):
        self.ps = pathSage.pathSage()

    def create_folder(self, folder_pn):
        if not self.ps.exists(folder_pn):
            os.mkdir(folder_pn)
        else:
            print("Folder already created.")

    def get_urls_w_pattern(self, url, pattern, exception):
        r = requests.get(url) # web url request launched
        soup = BeautifulSoup(r.text, 'html.parser') # return html script
        urls = []

        for link in soup.find_all('a'): # find all links in html page
            # if link contain a specific content (pattern) but has a different pattern of an exception, add it to a list
            # the * means that there is any characters after the pattern content
            if re.search(f'{pattern}*', link.get('href')) and link.get('href') not in urls and link.get('href') != exception:
                print(link.get('href'))
                urls.append(link.get('href'))

        return urls
    
    def is_corrupted_image(self, img_pne):
        try:
            Image.open(img_pne).verify()
            return True
        except Exception:
            print("Corrupted image!")
            self.ps.delete(img_pne)
            return False
    
    def is_corrupted_images(self, images_p):
        images_pne = self.ps.get_files_path(images_p, extension=[".jpg", ".png", ".jpeg"])

        for image_pne in images_pne: # for each items
            try:
                Image.open(image_pne).verify()
            except Exception:
                print(f"Corrupted image deleted!")
                self.ps.delete(image_pne) # if it didn't work, the script delete the image (using its path)

    def remove_images(self, images_p):
        images_pne = self.ps.get_files_path(images_p, extension=[".jpg", ".png", ".jpeg"])

        for image_pne in images_pne: # for each items
            self.ps.delete(image_pne)
