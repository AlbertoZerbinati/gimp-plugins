from gimpfu import *

def gestione_file(input_file, destination_file):
    # gets image and layer from input file
    image = pdb.gimp_file_load(input_file, input_file)
    drawable = pdb.gimp_image_get_active_layer(image)
    
    # saves it in the destination file
    pdb.gimp_message("Saving the image")
    pdb.gimp_file_save(image, drawable, destination_file, destination_file)
    
    # free memory
    pdb.gimp_image_delete(image)

register(
    'python-fu-gestione-file', 
    'Apre e salva un\'immagine', 
    'Non compie rielaborazioni, e\' un puro studio sulle funzionalita\' del linguaggio', 
    'AZ', 'AZ', '2021', 
    'Gestione file...', 
    '', 
    [
        (PF_FILE, "file", "Select input file", None), #an existing file
        (PF_FILENAME, "file", "Select output file", None), #a filename
    ], 
    [],
    gestione_file, menu="<Image>/MyScripts")

main()
