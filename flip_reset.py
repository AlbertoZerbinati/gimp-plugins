from gimpfu import *
#from gimpenums import ORIENTATION_HORIZONTAL


def flip_reset(image, drawable):
    pdb.gimp_message("flipping vertically")
    pdb.gimp_image_flip(image, ORIENTATION_VERTICAL)

register(
    'python-fu-flip-reset',
    'Flips image',
    'Flips the image 180 degrees vertically (upside-down). Basically executes a flip reset on the ball.',
    'AZ', 'AZ', '2021',
    'Flip reset',
    '',
    [
        (PF_IMAGE, "image", "Takes current image", None),
        (PF_DRAWABLE, "drawable", "Input layer", None)
    ],
    [],
    flip_reset, menu="<Image>/MyScripts")

main()
