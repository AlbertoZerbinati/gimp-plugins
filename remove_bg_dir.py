import os
from gimpfu import *

def remove_bg_dir(in_dir, out_dir):
    print "> Working on dir \"{}\"".format(in_dir)

    for in_file in os.listdir(in_dir):
		complete_name_infile = os.path.join(in_dir, in_file)
		print "  >> Working on file \"{}\"".format(complete_name_infile)
        
		if not (in_file.endswith('.png') or in_file.endswith('.PNG')):# or in_file.endswith('.jpg') or in_file.endswith('.jpeg')):
			print "   > Skipped non-png file \"{}\"\n".format(in_file)
			continue

		# gets image and layer from current input file
		image = pdb.gimp_file_load(complete_name_infile, in_file)
		drawable = image.layers[0]

		# apply effect on images:

		# add alpha channel to active layer for transaperncy
		#pdb.gimp_layer_add_alpha(drawable)

		# get background selection with color-picker on the top-left corner + by_bolor_selection
		x = 2
		y = 2
		sample_merged = FALSE
		sample_average = TRUE
		average_radius = 1
		color = pdb.gimp_color_picker(
		    image, drawable, x, y, sample_merged, sample_average, average_radius)

		threshold = 25
		operation = CHANNEL_OP_ADD
		antialias = TRUE
		feather = FALSE
		feather_radius = 0
		sample_merged = FALSE
		pdb.gimp_by_color_select(drawable, color, threshold, operation,
                         antialias, feather, feather_radius, sample_merged)

		#pdb.gimp_fuzzy_select(drawable, x, y, threshold, operation,
		# 					antialias, feather, feather_radius, sample_merged)

		# cut the selected region
		pdb.gimp_layer_add_alpha(drawable)
		
		#if not pdb.gimp_selection_is_empty:
		non_empty = pdb.gimp_edit_cut(drawable)

		# save image in the destination file
		pdb.gimp_file_save(image, drawable, out_dir + "\\" + in_file, in_file)

		print "   > File \"{}\" processed\n".format(in_file)
		# free memory
		pdb.gimp_image_delete(image)


register(
    'python-fu-remove-bg-dir',
    'Rimuove il colore di sfondo dalle immagini in una cartella e le salva in un\'altra',
    """Rimuove lo sfondo (se di un colore uniforme) delle foto formato png nella cartella input.
	   Salva poi le immagini ottenuta nella cartella di output""",
    'AZ', 'AZ', '2021',
    'Remove background directory...',
    '',
    [
        (PF_DIRNAME, "dir", "Select input directory", None),
        (PF_DIRNAME, "dir", "Select output directory", None),
    ],
    [],
    remove_bg_dir, menu="<Image>/MyScripts")

main()
