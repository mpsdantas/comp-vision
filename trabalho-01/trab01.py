import cv2 as cv2

import copy

import numpy as np

def read_img(caminho):
    return cv2.imread(caminho)

def show_img(img, title='Default'):
    cv2.imshow(title, img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def copy_img(img):
    return copy.copy(img)

def high_brightness(img, value=30):
    img_high_brightness = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    img[:,:,2] += value
    print(img.shape)
    return img

def create_vertiacal_lines_black(img, sizeLines = 10, spaceLine = 10):
    countBlack = 0
    countSpace = 0
    for x in range(img.shape[1]):
        if(countBlack <= sizeLines):
            img[:, x] = 0
            countBlack = countBlack + 1
        elif countSpace < spaceLine:
            countSpace = countSpace + 1
        else:
            countBlack = 0
            countSpace = 0
    return img

img = read_img('lena.png')

img_copy = copy_img(img)

img_copy = high_brightness(img_copy, 30)

img_copy = create_vertiacal_lines_black(img_copy, 10, 0)

show_img(img, 'Lena Original')

show_img(img_copy, 'Lena com mais brilho')