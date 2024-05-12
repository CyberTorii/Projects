import img2pdf
from pathSage import pathSage

class Convertor:
    def __init__(self):
        self.ps = pathSage.pathSage()

    def save_to_pdf(self, pdf_n, images_p, save_p):
        images_pne = self.ps.get_files_path(images_p, extension=[".jpg", ".png", ".jpeg"])
        # images_pne = self.ps.get_files_path(images_p, extension=[".jpg"])
        images_pne = sorted(images_pne, key=self.custom_sort)

        if images_pne:
            with open(f"{save_p}{pdf_n}.pdf","wb") as f:
                print("\nConverting to pdf...")
                f.write(img2pdf.convert(images_pne)) # write a pdf by converting all images in the list

    def custom_sort(self, item):
        chap, page = self.ps.stem(item).split(';')
        return (int(chap), int(page))