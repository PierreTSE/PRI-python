import easyocr
from pprint import pp
from src import utils

def ocr(img):
    reader = easyocr.Reader(lang_list=['en', 'fr'],
                            download_enabled=False)
    return reader.readtext(image=img,
                           canvas_size=720)


if __name__ == '__main__':
    pp(ocr(str(utils.path_from_root("image_samples/IMG_7317.JPG"))))