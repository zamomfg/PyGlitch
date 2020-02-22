#!/urs/bin/python

import sys, getopt, os, argparse
import numpy as np
from PIL import Image, ImageFilter


def glitch(image_path):
    path = os.path.abspath(image_path)
    print(path)
    image = Image.open(path)
    print(image)
    pixels = np.asarray(image)
    # pixels = image.load()
    x_size = len(pixels[:,1])
    y_size = len(pixels[1,:])
    # i = 0
    # for col in pixels:
    #     print(col[0])
    #     print(i)
    #     i += 1
    get_pixels_in_square(0, 0, 10, 10, pixels)

# get the pixels from the square from the npmyp array "image"
def get_pixels_in_square(ax, ay, bx, by, pixels):
    # x_size =  bx - ax
    # y_size = by - ay
    # print(x_size, y_size)
    # matrix = np.empty((x_size, y_size))
    # index_x = 0
    # index_y = 0
    # for i in range(ax, bx):
    #     for j in range(ay, by):
    #         print("[{0}] [{1}] {2}".format(i, j, pixels[i,j]))
    #         matrix[index_x,index_y] = pixels[i,j]
    #         index_y += 1
    #     index_x += 1
    print(pixels[ay:by, ax:bx])


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-i", help="The path to the input image")
    parser.add_argument("-o", help= "The output path")
    args = parser.parse_args()
    glitch(args.i)

