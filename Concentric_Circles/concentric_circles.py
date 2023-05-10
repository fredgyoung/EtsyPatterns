"""
https://pillow.readthedocs.io/en/stable/reference/index.html
"""
from PIL import Image, ImageDraw, ImageColor
# from palettes.pastels import offeo_pastels
# from palettes.html_colors import html_named_colors

OUTPUT_FOLDER = './Output/'
TITLE = 'Circles'
# COLORS = html_named_colors
DPI = 300
WIDTH, HEIGHT = 3600, 3600
CIRCLES = [
    {'color': 'red', 'radius': 250},
    {'color': 'orange', 'radius': 200},
    # {'color': 'yellow', 'radius': 200},
    {'color': 'green', 'radius': 150},
    {'color': 'blue', 'radius': 100},
    {'color': 'purple', 'radius': 50},
]


def draw_circles(canvas):

    for y_center in range(0, 3600+1, 600):
        for x_center in range(0, 3600+1, 600):
            for circle in CIRCLES:
                x0 = x_center - circle['radius']
                x1 = x_center + circle['radius']
                y0 = y_center - circle['radius']
                y1 = y_center + circle['radius']

                canvas.ellipse([(x0, y0), (x1, y1)], fill=ImageColor.getrgb(circle['color']))


if __name__ == '__main__':

    img = Image.new('RGB', (WIDTH, HEIGHT), ImageColor.getrgb('white'))
    c = ImageDraw.Draw(img)
    draw_circles(c)
    img.save('./Output/con_circles.jpg', "JPEG", dpi=(300, 300))
