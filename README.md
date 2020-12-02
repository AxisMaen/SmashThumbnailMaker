# Melee Thumbnail Maker

This is a Python plugin for Gimp that allows for easy, customizable creation of Melee thumbnails.

## Installation

Make sure you have GIMP installed.  
https://www.gimp.org/downloads/

Find your Gimp plug-ins folder. This is typically located in "C:\Program Files\GIMP 2\lib\gimp\2.0\plug-ins".   
If you can't find the folder, open Gimp and go to Edit > Preferences > Folders > Plugins to find it. 

Drag the thumbnail.py file into the plug-ins folder and restart Gimp if you have it open. If correctly installed, you should see "Smash Thumbnails..." in Gimp under the Filters > Enhance menu.

## Usage

Open template.xcf in Gimp. Select the topmost layer (can sometimes have weird results if you don't do this, will fix) and go to to Filters > Enhance > Smash Thumbnails. Enter the information you want and hit create. Character 1 is left and character 2 is right.  
Each character has two layers (e.g. Fox 1 & Fox 2). For each character, make sure to select the correct number. For example, the first character should be something like "Fox 1", not "Fox 2". I hope to clean this up in the future so it's not as confusing. 

## Customization

You can edit the "Top", "Bot", "Middle", "Logo", "Event Logo", and "VS" layers to be whatever you want. They will stay static across every thumbnail. Make sure you do not change the layer names or they will be made invisible when you create a thumbnail. If you want to change layer names or add new static layers, go to the thumbnail.py and add/change the values in the staticLayers array. Make sure to restart Gimp every time you change the plugin code.  

To change the positions of text you have two options.  
1. Create the thumbnail and move things manually with the move tool in Gimp for each thumbnail.  
2. Open thumbnail.py and change the values of the offsets and centers at the top of the file. This will take some playing around with to find the right values, but once you find the right values it should be easier to mass produce thumbnails from then on.

To change the positions of characters, just select the character layer in Gimp and move it to the spot you want manually. Characters will not shift from this spot when a thumbnail is made, so they will be effectively static.

I'm hoping to make customizing the positions of each text layer and character easier in the future.