
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

PRIMARY = "#e8cd7e"     # "gold"
SECONDARY = "#6c3c86"  # "purple"    # "white"
TERTIARY = "white"

images = [
    {"name": "circles", "file": "./images/circle.png"},
    {"name": "hearts", "file": "./images/heart.png"},
    {"name": "h_lines", "file": "./images/h_lines.png"},
    {"name": "quatrefoils", "file": "./images/quatrefoil.png"},
    {"name": "scallops", "file": "./images/scallop.png"},
    {"name": "stars", "file": "./images/star.png"},
    {"name": "starburst", "file": "./images/starburst.png"},
    {"name": "diamond", "file": "./images/diamond.png"},
]

for image in images:
    input_file = image["file"]
    output_file = f"./output/" + image["name"] + ".png"
    inp = Image.open(input_file).convert("L")
    out = ImageOps.colorize(inp, black=PRIMARY, white=SECONDARY)
    # out.show()
    out.save(output_file, "PNG")

