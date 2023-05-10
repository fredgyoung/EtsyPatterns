
from PIL import Image, ImageOps, ImageColor

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
IMAGE_DIRECTORY = "./images"
OUTPUT_DIRECTORY = "./output"

masks = [
    {"name": "circles", "file": f"{IMAGE_DIRECTORY}/circle.png"},
    {"name": "hearts", "file": f"{IMAGE_DIRECTORY}/heart.png"},
    {"name": "h_lines", "file": f"{IMAGE_DIRECTORY}/h_lines.png"},
    {"name": "quatrefoils", "file": f"{IMAGE_DIRECTORY}/quatrefoil.png"},
    {"name": "scallops", "file": f"{IMAGE_DIRECTORY}/scallop.png"},
    {"name": "stars", "file": f"{IMAGE_DIRECTORY}/star.png"},
    {"name": "starburst", "file": f"{IMAGE_DIRECTORY}/starburst.png"},
    {"name": "diamond", "file": f"{IMAGE_DIRECTORY}/diamond.png"},
]

for image in masks:
    background = Image.open("./images/purple.png")
    foreground = Image.open("./images/gold_gradient.png")
    mask = Image.open(f"{image['file']}").convert('L')
    new_file = Image.composite(background, foreground, mask)
    new_file.save(f"{OUTPUT_DIRECTORY}/{image['name']}.png", "PNG")
