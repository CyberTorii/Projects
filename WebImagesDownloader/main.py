import downloader
import img_to_pdf
import tools
from pathSage import pathSage
from pathlib import Path

class Main:
    def __init__(self):
        self.ps = pathSage.pathSage()
        self.dw = downloader.Downloader()
        self.i2p = img_to_pdf.Convertor()
        self.tool = tools.Tools()
        
        self.ROOT = Path().cwd()
        self.IMAGES_P = self.ps.as_new_path(self.ps.join(self.ROOT, ["Images"]))
        self.PDF_P = self.ps.as_new_path(self.ps.join(self.ROOT, ["Ebook"]))

        self.tool.create_folder(self.IMAGES_P)
        self.tool.create_folder(self.PDF_P)
        self.main_2()

    def main(self):
        page = 1
        chap = 20
        for c in range(chap):
            for p in range(page):
                norm_p = str(p+1).rjust(3, '0')
                norm_c = str(c+1).rjust(4, '0')
                
                img_url = f"https://url/{norm_c}/{norm_p}.jpg"
                img_ne = f"{c+1};{p+1}.{img_url.rsplit('.', 1)[1]}"
                
                self.dw.download_one_img(img_url, img_ne, self.IMAGES_P)
        
        self.i2p.save_to_pdf("amongst_us", self.IMAGES_P, self.PDF_P)
        self.tool.remove_images(self.IMAGES_P)
        print("Good read !")

    def main_2(self):
        page = 1
        chap = 116-15
        good = True
        for c in range(chap):
            while good:
                norm_p = str(page).rjust(3, '0')
                norm_c = c+15 # str(c+1).rjust(4, '0')
        
                img_url = f"https://url/{norm_c}/{norm_p}.jpg"
                img_ne = f"{norm_c};{norm_p}.{img_url.rsplit('.', 1)[1]}"

                good = self.dw.download_one_img(img_url, img_ne, self.IMAGES_P)
                page += 1
            
            self.i2p.save_to_pdf(f"manga_name_{norm_c-15+1}", self.IMAGES_P, self.PDF_P)
            self.tool.remove_images(self.IMAGES_P)
            good = True
            page = 1
        
        print("Good read !")

main = Main()