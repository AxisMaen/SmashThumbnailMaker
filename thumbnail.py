#!/usr/bin/env python

# GIMP Python plug-in template.

from gimpfu import *

def do_stuff(img, char1, char2) :
    #gimp.progress_init("Doing stuff to " + layer.name + "...")

    # Set up an undo group, so the operation will be undone in one step.
    pdb.gimp_undo_push_group_start(img)
	
	#make all layers invisible to start
    for layer in gimp.image_list()[0].layers:
        layer.opacity = 0.0
		
	#if it is the char we want, make it visible
    char1.opacity = 100.0
    char2.opacity = 100.0
	
    # Close the undo group.
    pdb.gimp_undo_push_group_end(img)

register(
    "python_fu_do_stuff",
    "Smash Thumbnail Maker",
    "A python plugin for gimp that allows for easy creation of thumbnails",
    "Matthew Rodgers",
    "Matthew Rodgers",
    "2019",
    "Thumbnails...",
    "*",      # Alternately use RGB, RGB*, GRAY*, INDEXED etc.
    [	
		(PF_IMAGE, "img", "Input image", None),
        (PF_LAYER, "char1", "Character 1 Layer", None),
		(PF_LAYER, "char2", "Character 2 Layer", None)
    ],
    [],
    do_stuff, menu="<Image>/Filters/Enhance")

main()