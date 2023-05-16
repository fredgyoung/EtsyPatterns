import os
import pathlib
import zipfile

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
    "White"
]


def create_zip_file(colour):

    directory = pathlib.Path(f"./output/Gold_on_{colour}/")

    zip_file_name = f"./output/Zip_Files/Gold_on_{colour}.zip"

    # If zip file exists, delete it
    if os.path.exists(zip_file_name):
        os.remove(zip_file_name)

    # Create zip file
    file = open(zip_file_name, "x")
    file.close()

    # Add files to zip file
    with zipfile.ZipFile(zip_file_name, mode="w") as archive:
        for file_path in directory.iterdir():
            archive.write(file_path, arcname=file_path.name)

    # Read zip file
    with zipfile.ZipFile(zip_file_name, mode="r") as archive:
        archive.printdir()


if __name__ == '__main__':

    for color in colors:
        create_zip_file(color)
