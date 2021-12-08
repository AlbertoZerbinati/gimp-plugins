import os, sys
from gimpfu import *
from remove_bg import remove_bg


def run_on_dir(dire):
    print "> Working on dir \"{}\"".format(dire)

    for infile in os.listdir(dire):
		complete_name_infile = os.path.join(dire, infile)
		print "  >> Working on file \"{}\"".format(complete_name_infile)

		if not (infile.endswith('.png') or infile.endswith('.PNG')):
			print "   > Skipped non-png/file \"{}\"\n".format(infile)
			continue

		# gets image and layer from current input file
		image = pdb.gimp_file_load(complete_name_infile, infile)
		drawable = pdb.gimp_image_get_active_layer(image)

		#apply effect on images
		outfile = dire + "processed" + infile



		print "   > File \"{}\" processed\n".format(infile)
		# free memory
		pdb.gimp_image_delete(image)
