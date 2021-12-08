#!/usr/bin/env python

# Tutorial available at: https://www.youtube.com/watch?v=nmb-0KcgXzI
# Feedback welcome: jacksonbates@hotmail.com

from gimpfu import *

def hello_warning():
    # function code goes here...
    pdb.gimp_message("Hello, World!")
    

register(
    "python-fu-hello-warning",
    "Hello world warning",
    "Prints 'Hello, world!' to the error console",
    "Jackson Bates", "Jackson Bates", "2015",
    "Hello warning",
    "", # type of image it works on (*, RGB, RGB*, RGBA, GRAY etc...)
    [
        #(PF_IMAGE, "image", "takes current image", None),
        #(PF_DRAWABLE, "drawable", "Input layer", None)
    ],
    [],
    hello_warning, menu="<Image>/MyScripts")  # second item is menu location

main()