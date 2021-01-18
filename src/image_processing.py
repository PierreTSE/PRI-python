import cv2 as cv


def read_image(path):
    img = cv.imread(str(path))
    if img is None:
        raise IOError("Could not read an image from " + path)
    return img
