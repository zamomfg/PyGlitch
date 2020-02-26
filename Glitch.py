#!/urs/bin/python

import sys, getopt, os, argparse, random, time
import numpy as np
from PIL import Image, ImageFilter

image = None
in_pixels = None
out_pixels = None
x_size = 0
y_size = 0

def glitch(image_path, distort_amount):
    global image
    global in_pixels
    global out_pixels
    global x_size
    global y_size
    path = os.path.abspath(image_path)
    image = Image.open(path)
    in_pixels = np.asarray(image)
    y_size = len(in_pixels[:,1])
    x_size = len(in_pixels[1,:])

    out_pixels = np.array(image)

    max_distort = min(20, distort_amount)
    number_of_shifts = random.randint(1, max_distort)
    print("number of shifts {0}".format(number_of_shifts))

    for i in range(0,number_of_shifts):
        distance = random.randint(1,int(x_size*0.75))
        y_pos = random.randint(1,y_size)
        direction = random.randint(0,1) == 0
        # offset_pixels_horizontal(shift_rgb_layers(in_pixels), direction, distance, y_pos)
        offset_pixels_horizontal(in_pixels, direction, distance, y_pos)
    # offset_pixels_horizontal(True, 100, 204)
    out_image = Image.fromarray(out_pixels, image.mode)
    out_image.show()


def offset_pixels_horizontal(pixel_matrix, right, shift_distace, y_pos):
    global out_pixels
    Y_HEIGHT_DIVIDER = 5
    y_start_pos = random.randint(0, y_size)
    y_height = random.randint(1, y_size / Y_HEIGHT_DIVIDER)
    y_stop_pos = y_start_pos + y_height

    x_start_pos = shift_distace
    x_stop_pos = x_size - x_start_pos

    pixel_square = None
    wraped_square = None
    # shift_rgb_layers()
    if right:
        pixel_square = pixel_matrix[y_start_pos : y_stop_pos, :x_stop_pos]
        wraped_square = pixel_matrix[y_start_pos : y_stop_pos, x_stop_pos:]
        
        out_pixels[y_start_pos : y_stop_pos, x_start_pos:] = pixel_square
        out_pixels[y_start_pos : y_stop_pos, :x_start_pos] = wraped_square
    else:
        pixel_square = pixel_matrix[y_start_pos : y_stop_pos, x_start_pos:]
        wraped_square = pixel_matrix[y_start_pos : y_stop_pos, :x_start_pos]

        out_pixels[y_start_pos : y_stop_pos, :x_stop_pos] = pixel_square
        out_pixels[y_start_pos : y_stop_pos, x_stop_pos:] = wraped_square

def shift_rgb_layers(pixel_matrix):
    y_size = len(pixel_matrix[:,1])
    x_size = len(pixel_matrix[1,:])
    # layer = get_rgb_layer()

    # y_shift = random.randint(1, 150)
    # x_shift = random.randint(1, 150)

    # y_start = y_shift
    # y_stop = y_start + y_size
    # x_start = x_shift
    # x_stop = x_size - x_start

    rgb_layer = get_rgb_layer()
    print("layer {0}".format(rgb_layer))
    r,g,b = np.dsplit(pixel_matrix,pixel_matrix.shape[-1])
    if rgb_layer == 0:
        g = np.empty([y_size,x_size,1], dtype=np.uint8)
        b = np.empty([y_size,x_size,1], dtype=np.uint8)
    elif rgb_layer == 1:
        r = np.empty([y_size,x_size,1], dtype=np.uint8)
        b = np.empty([y_size,x_size,1], dtype=np.uint8)
    elif rgb_layer == 2:
        r = np.empty([y_size,x_size,1], dtype=np.uint8)
        g = np.empty([y_size,x_size,1], dtype=np.uint8)

    im = np.dstack((r,g,b))
    print(im)

    return im

def get_rgb_layer():
    return random.randint(0,3)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-i", help="The path to the input image")
    parser.add_argument("-o", help= "The output path")
    parser.add_argument("-s", help="Set the seed for the random generator that controlls the distortion of the image")
    args = parser.parse_args()
    if args.s:
        random.seed(args.s)
    else:
        random.seed(time.time())

    distort_amount = random.randint(40,134)
    glitch(args.i, distort_amount)