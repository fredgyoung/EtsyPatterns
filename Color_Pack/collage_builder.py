"""
https://pillow.readthedocs.io/en/stable/reference/index.html
"""
import os
from PIL import Image

colors = [
    "Aqua",
    "Black",
    "Coral",
    "Navy",
    "Pink",
    "Purple",
    "Red",
    "RoyalBlue",
    "Turquoise",
]


def create_collage(primary_color):

    new_image = Image.new('RGBA', (3600, 3600), color=(255, 255, 255, 255))

    collage_directory = "./output/Collages/"
    colored_file_directory = f"./output/Gold_on_{primary_color}/"
    white_file_directory = "./output/Gold_on_White/"

    colored_file_list = os.listdir(colored_file_directory)
    white_file_list = os.listdir(white_file_directory)

    print(colored_file_list)
    print(white_file_list)

    mixed_file_list = []

    while colored_file_list or white_file_list:

        if colored_file_list:
            file = colored_file_directory + colored_file_list.pop()
            print(file, os.path.isfile(file), file[-3:])
            if os.path.isfile(file) and file[-3:] == "jpg":
                mixed_file_list.append(file)

        if white_file_list:
            file = white_file_directory + white_file_list.pop()
            print(file, os.path.isfile(file), file[-3:])
            if os.path.isfile(file) and file[-3:] == "jpg":
                mixed_file_list.append(file)

    print(mixed_file_list)

    for index, file in enumerate(mixed_file_list[:]):
        with Image.open(f"{file}") as im:
            left = (index // 2) * 450
            right = left + 450
            if index % 4 == 0 or index % 4 == 3:
                top = 0
            else:
                top = 1800
            bottom = top + 1800
            cropped_image = im.crop((left, top, right, bottom))
            new_image.paste(cropped_image, box=(left, top, right, bottom), mask=None)

    shadow = Image.open("./images/shadow.png")
    collage = Image.alpha_composite(new_image, shadow)
    collage.save(f"{collage_directory}/{primary_color}_collage.png", "PNG", dpi=(300, 300))


if __name__ == '__main__':

    print(f"INFO: in main")

    for color in colors:
        print(f"INFO: color = {color}")
        create_collage(color)

else:

    print(f"INFO: wrong")
