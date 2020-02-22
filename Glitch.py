#!/urs/bin/python

import sys, getopt, os, argparse
from PIL import Image, ImageFilter

def glitch(image_path):
    print(image_path)
    

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-i", help="The path to the input image")
    parser.add_argument("-o", help= "The output path")
    args = parser.parse_args()
    glitch(args.i)

