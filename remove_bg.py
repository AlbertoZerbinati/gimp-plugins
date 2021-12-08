from gimpfu import *


def remove_bg(image, drawable, out_file):
	# add alpha channel to active layer for transaperncy
	pdb.gimp_layer_add_alpha(drawable)

	# get background selection with the fuzzy tool applied on the top-left corner
	x = 2
	y = 2
	threshold = 35
	operation = CHANNEL_OP_ADD
	antialias = TRUE
	feather = FALSE
	feather_radius = 0
	sample_merged = FALSE
	pdb.gimp_fuzzy_select(drawable, x, y, threshold, operation, 
						  antialias, feather, feather_radius, sample_merged)
						  
	# cut the selected region
	non_empty = pdb.gimp_edit_cut(drawable)

	# save image in the destination file
	#pdb.gimp_message("Saving the image")
	pdb.gimp_file_save(image, drawable, out_file, out_file)


register(
    'python-fu-remove-bg',
    'Rimuove il colore di sfondo da un\'immagine',
    """Rimuove lo sfondo della foto, se di un colore uniforme, rendendolo trasparente.
	   Salva poi l\'immagine ottenuta nel file indicato""",
    'AZ', 'AZ', '2021',
    'Remove background...',
    '',
    [
        (PF_IMAGE, "image", "Current image", None),
        (PF_DRAWABLE, "drawable", "Current layer", None),
		(PF_FILENAME, "filename", "Output filename", None)
    ],
    [],
    remove_bg, menu="<Image>/MyScripts")

main()
