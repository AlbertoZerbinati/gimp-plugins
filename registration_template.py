#!/usr/bin/env python

# Tutorial available at: https://www.youtube.com/watch?v=nmb-0KcgXzI
# Feedback welcome: jacksonbates@hotmail.com
# ALL RIGHTS RESEVRVED TO THIS MAN
# only useful in order to make gui scripts, they seem not to run in console if they need parameters 
#(for example I can't pass them the file containing the image to manipulate)

from gimpfu import *

def NAME_OF_MAIN_FUNCTION(image, drawable): #"mandatory" arguments, then you can add optional ones
    # function code goes here...
    

register(
    "python-fu-NAME-OF-MAIN-FUNCTION",
    "SHORT DESCRIPTION",
    "LONG DESCRIPTION",
    "AZ", "AZ", "2021",
    "NAME FOR MENU",
    "", # type of image it works on (*, RGB, RGB*, RGBA, GRAY etc...)
    [
        # basic parameters are: (UI_ELEMENT, "variable", "label", Default)
        (PF_IMAGE, "image", "Takes current image", None),
        (PF_DRAWABLE, "drawable", "Input layer", None)
        # PF_SLIDER, SPINNER have an extra tuple (min, max, step)
        # PF_RADIO has an extra tuples within a tuple:
        # eg. (("radio_label", "radio_value), ...) for as many radio buttons
        # PF_OPTION has an extra tuple containing options in drop-down list
        # eg. ("opt1", "opt2", ...) for as many options
        # see ui_examples_1.py and ui_examples_2.py for live examples
    ],
    [],
    NAME_OF_MAIN_FUNCTION, menu="<Image>/MyScripts")  # second item is menu location

main() #activates this scripts functionality