import os
import sys
from gimpfu import *



def gestione_dir(input_dir, destination_dir):
    print "> Working on dir \"{}\"".format(input_dir)

    for infile in os.listdir(input_dir):
        complete_name_infile = os.path.join(input_dir, infile)

        print "  >> Working on file \"{}\"".format(complete_name_infile)

        if (not infile.endswith('.png')) and (not infile.endswith('.jpeg')) and (not infile.endswith('.jpg')):
            print "   > Skipped non-png/jpeg/jpg file \"{}\"\n".format(infile)
            continue

        # gets image and layer from current input file
        image = pdb.gimp_file_load(complete_name_infile, infile)
        drawable = pdb.gimp_image_get_active_layer(image)

        # apply cubism effect
        tile_size = 6.0
        tile_saturation = 3.5
        bg_color = 0.0
        pdb.plug_in_cubism(image, drawable, tile_size,
                           tile_saturation, bg_color)

        # saves image in the destination file
        outfile = "processed " + infile
        complete_name_outfile = os.path.join(destination_dir, outfile)
        pdb.gimp_file_save(image, drawable, complete_name_outfile, outfile)

        print "   > File \"{}\" processed\n".format(infile)
        # free memory
        pdb.gimp_image_delete(image)

    pdb.gimp_message("Succesfully completed!")


register(
    'python-fu-gestione-dir',
    'Apre una cartella e salva le immagini ivi contenute in un\'altra cartella, dopo aver applicato il filtro cubism a ciascuna',
    'Un puro studio sulle funzionalita\' del linguaggio',
    'AZ', 'AZ', '2021',
    'Gestione directory...',
    '',
    [
        (PF_DIRNAME, "dir", "Select input directory", None),
        (PF_DIRNAME, "dir", "Select output directory", None),
    ],
    [],
    gestione_dir, menu="<Image>/MyScripts")

main()
