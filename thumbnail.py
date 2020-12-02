#!/usr/bin/env python

# GIMP Python plug-in template.

from gimpfu import *

def do_stuff(img, eventNum, roundName, player1, char1, player2, char2, txtColor, font) :
    #gimp.progress_init("Doing stuff to " + layer.name + "...")

    #these layers are consistent across every thumbnail
    staticLayers = ["Top", "Bottom", "Middle", "Logo", "Event Logo", "VS"]
    
    #vertical offset for player names
    vertOffsetDefault = 25
    fontSizeDefault = 90
    
    #horizontal "center" for player names
    p1Center = 300
    p2Center = 970
    
    #horizontal "center" and offsets for round name
    roundNameCenter = 620
    roundNameHorOffset = 25
    roundNameVertOffset = 590

    # Set up an undo group, so the operation will be undone in one step.
    pdb.gimp_undo_push_group_start(img)

    #make all chars invisible to start
    for layer in gimp.image_list()[0].layers:
        if(layer.name not in staticLayers):
            layer.visible = False
		
	#make the chars we want visible
    char1.visible = True
    char2.visible = True
	
	# Set the text color
    gimp.set_foreground(txtColor)
	
	#set player 1 text size
    fontSize = fontSizeDefault
    vertOffset = vertOffsetDefault
    
    #lazily accounting for long tags (will improve later)
    if(len(player1) > 6):
        fontSize = fontSizeDefault - 10
        vertOffset = vertOffset + 5
    if(len(player1) > 8):
        fontSize = fontSizeDefault - 15
        vertOffset = vertOffset + 5
	
	#creating and shifting the player 1 name
    player1Layer = pdb.gimp_text_fontname(img, None, 0, 0, player1, 10, True, fontSize, PIXELS, font)
    player1Layer.translate(p1Center - player1Layer.width/2, vertOffset)
    
    #some extra shifting if long tag (lazy)
    if(len(player1) > 8):
        player1Layer.translate(player1Layer.width/15, 0)
    
    
	#set player 2 text size
    fontSize = fontSizeDefault
    vertOffset = vertOffsetDefault
    
    #lazily accounting for long tags (will improve later)
    if(len(player2) > 6):
        fontSize = fontSizeDefault - 10
        vertOffset = vertOffset + 5
    if(len(player2) > 8):
        fontSize = fontSizeDefault - 15
        vertOffset = vertOffset + 5
        
	#creating and shifting the player 2 name
    player2Layer = pdb.gimp_text_fontname(img, None, 0, 0, player2, 10, True, fontSize, PIXELS, font)
    player2Layer.translate(p2Center - player2Layer.width/2, vertOffset)
    
    #some extra shifting if long tag (lazy)
    if(len(player2) > 8):
        player2Layer.translate(-player2Layer.width/15, 0)
    
    #creating the event number layer
    eventNumLayer = pdb.gimp_text_fontname(img, None, 10, 630, eventNum, 10, True, 70, POINTS, font)
    
    #creating and shifting the round name layer
    roundNameLayer = pdb.gimp_text_fontname(img, None, roundNameHorOffset, roundNameVertOffset, roundName, 10, True, 80, POINTS, font)  
    roundNameLayer.translate(roundNameCenter - roundNameLayer.width/2, 0)
    
    # Close the undo group.
    pdb.gimp_undo_push_group_end(img)

register(
    "python_fu_do_stuff",
    "Smash Thumbnail Maker",
    "A python plugin for gimp that allows for easy creation of thumbnails",
    "Matthew Rodgers",
    "Matthew Rodgers",
    "2019",
    "Smash Thumbnails...",
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