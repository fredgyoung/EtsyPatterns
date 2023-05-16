"""
diagonal_stripes
circles
scallops
broken_chevron
hearts
chevron
stars
clovers
horizontal_stripes
"""
"""
Makes the directories and the pattern files 
Colorizes black and white images
"""

import os
from PIL import Image, ImageColor, ImageOps


IMAGE_DIRECTORY = "./images"
OUTPUT_DIRECTORY = "./output"

CIRCLE_MASK = {"name": "circles", "file": "./images/circle.png"}
HEART_MASK = {"name": "hearts", "file": "./images/heart.png"}
LINES_MASK = {"name": "h_lines", "file": "./images/h_lines.png"}
QUATREFOIL_MASK = {"name": "quatrefoils", "file": "./images/quatrefoil.png"}
SCALE_MASK = {"name": "scallops", "file": "./images/scallop.png"}
STAR_MASK = {"name": "stars", "file": "./images/star.png"}
STARBURST_MASK = {"name": "starburst", "file": "./images/starburst.png"}
DIAMOND_MASK = {"name": "diamonds", "file": "./images/diamond.png"}

colors = [
    "Aqua",
    "Black",
    "Coral",
    # "Lilac",
    "Navy",
    "Pink",
    "Purple",
    "Red",
    "RoyalBlue",
    # "SoftPink",
    "Turquoise",
    "White"
]

masks = [
    CIRCLE_MASK,
    HEART_MASK,
    LINES_MASK,
    QUATREFOIL_MASK,
    SCALE_MASK,
    STAR_MASK,
    STARBURST_MASK,
    DIAMOND_MASK
]

for color in colors:

    output_directory = f"./output/Gold_on_{color}"

    # Create directory
    if not os.path.exists(output_directory):
        os.mkdir(output_directory)
        print(f"Making directory: {output_directory}")

    for image in masks:
        # Open files
        colored_image = Image.new('RGB', (3600, 3600), ImageColor.getrgb(color))
        gold_image = Image.open("./images/gold_gradient.png")
        white_image = Image.new('RGB', (3600, 3600), ImageColor.getrgb('white'))
        mask_image = Image.open(f"{image['file']}").convert('L')

        # gold foreground & colored background
        filename = f"{output_directory}/Gold_on_{color}_{image['name']}.png"
        new_file = Image.composite(colored_image, gold_image, mask_image)
        new_file.save(filename, "PNG")



