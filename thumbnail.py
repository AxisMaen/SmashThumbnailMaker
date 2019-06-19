#!/usr/bin/env python

# GIMP Python plug-in template.

from gimpfu import *

def do_stuff(img, char1, char2) :
    gimp.progress_init("Doing stuff to " + layer.name + "...")

    # Set up an undo group, so the operation will be undone in one step.
    pdb.gimp_undo_push_group_start(img)

    # Do stuff here.
    pdb.gimp_invert(layer)

    # Close the undo group.
    pdb.gimp_undo_push_group_end(img)

register(
    "python_fu_do_stuff",
    "Do stuff",
    "Longer description of doing stuff",
    "Your Name",
    "Your Name",
    "2010",
    "Do Stuff...",
    "*",      # Alternately use RGB, RGB*, GRAY*, INDEXED etc.
    [	
		(PF_IMAGE, "img", "Input image", None),
        (PF_LAYER, "char1", "Character 1 Layer", None),
		(PF_LAYER, "char2", "Character 2 Layer", None)
    ],
    [],
    do_stuff, menu="<Image>/Filters/Enhance")

main()