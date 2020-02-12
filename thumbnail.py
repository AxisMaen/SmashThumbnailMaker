#!/usr/bin/env python

# GIMP Python plug-in template.

from gimpfu import *

def do_stuff(img, eventNum, roundName, player1, char1, player2, char2, txtColor, font) :
    #gimp.progress_init("Doing stuff to " + layer.name + "...")

    # Set up an undo group, so the operation will be undone in one step.
    pdb.gimp_undo_push_group_start(img)
    

    #make all chars invisible to start
    for layer in gimp.image_list()[0].layers:
        if(layer.name != "BG" and layer.name != "Top Dark"
           and layer.name != "Bot Dark" and layer.name != "Laser BG"
           and layer.name != "Logo" and layer.name != "VS" 
		   and layer.name != "Event Logo"):
            layer.visible = False
		
	#make the chars we want visible
    char1.visible = True
    char2.visible = True
	
	# Set the text color
    gimp.set_foreground(txtColor)
	
	#set player 1 text size
    fontSize = 90 #default size
    vertOffset = 25
    if(len(player1) > 6):
        fontSize = 80
        vertOffset = 30
    if(len(player1) > 8):
        fontSize = 75
        vertOffset = 30
	
	
    player1Layer = pdb.gimp_text_fontname(img, None, 0, 0, player1, 10, True, fontSize, PIXELS, font)
    player1Layer.translate(300-player1Layer.width/2, vertOffset)
    
    if(len(player1) > 8):
        player1Layer.translate(player1Layer.width/15, 0)
    
    
    
    
	#set player 2 text size
    fontSize = 90 #default size
    vertOffset = 25
    if(len(player2) > 6):
        fontSize = 80
        vertOffset = 30
    if(len(player2) > 8):
        fontSize = 75
        vertOffset = 30
        
	
    player2Layer = pdb.gimp_text_fontname(img, None, 0, 0, player2, 10, True, fontSize, PIXELS, font)
    player2Layer.translate(970-player2Layer.width/2, vertOffset)
    
    #some extra shifting if long tag
    if(len(player2) > 8):
        player2Layer.translate(-player2Layer.width/15, 0)
    #p2 center = 970
    
    eventNumLayer = pdb.gimp_text_fontname(img, None, 10, 630, eventNum, 10, True, 70, POINTS, font)
    
    roundNameLayer = pdb.gimp_text_fontname(img, None, 25, 590, roundName, 10, True, 80, POINTS, font)
    
    roundNameLayer.translate(620-roundNameLayer.width/2, 0)
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
        (PF_STRING, "word", "Event Number", "##"),
        (PF_STRING, "word", "Round Name", "Winners Finals"),
		(PF_STRING, "word", "Player 1", "Mango"),
        (PF_LAYER, "char1", "Character 1 Layer", None),
        (PF_STRING, "word", "Player 2", "Armada"),
		(PF_LAYER, "char2", "Character 2 Layer", None),
        (PF_COLOR, "txtColor", "Text color", (1.0, 1.0, 1.0)),
        (PF_FONT, "font", "Font face", "BatmanForeverAlternate")
    ],
    [],
    do_stuff, menu="<Image>/Filters/Enhance")

main()