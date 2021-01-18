import cv2 as cv


def read_image(path, flag=cv.IMREAD_COLOR):
    img = cv.imread(str(path), flag)
    if img is None:
        raise IOError("Could not read an image from " + path)
    return img
