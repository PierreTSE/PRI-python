from collections.abc import Sequence
from pprint import pp
import easyocr
import numpy as np
from src import utils


def convert(o):
    if isinstance(o, np.int64) or isinstance(o, np.int32):
        return int(o)
    return o


def recursive_map(seq, func):
    for item in seq:
        if isinstance(item, Sequence):
            yield type(item)(recursive_map(item, func))
        else:
            yield func(item)


def format_response(ocr_res):
    response = [
        {
            "boxes": list(recursive_map(e[0], convert)),
            "result": e[1],
            "confidence": e[2]
        }
        for e in ocr_res
    ]
    return response


def ocr(img):
    reader = easyocr.Reader(lang_list=['en', 'fr'],
                            download_enabled=False)
    return reader.readtext(image=img,
                           canvas_size=720)
