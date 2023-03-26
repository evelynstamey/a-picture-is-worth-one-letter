from datetime import datetime
import ipyplot
import json
import logging
from os.path import dirname, abspath
import random
from string import ascii_uppercase

from letters_speaking.image_draw import draw_text_image
from letters_speaking.color_library import COLOR_LIBRARY, GROUNDS


logging.basicConfig(level=logging.INFO)
_log = logging.getLogger(__name__)

# Set defaults
ARTIFACTS_DIR = f"{dirname(dirname(abspath(__file__)))}/artifacts"
FONTS_DIR = f"{dirname(dirname(dirname(abspath(__file__))))}/Library/Fonts"
FONT_FILE = "Comic Sans MS.ttf"
CANVAS_SIZE = 120


def _get_color(color=None, style=None, ground=None):
    if color:
        return color
    if style:
        return random.choice(COLOR_LIBRARY[style])
    _bg_style, _fg_style = random.choice(GROUNDS)
    if ground == "bg":
        return random.choice(COLOR_LIBRARY[_bg_style])
    if ground == "fg":
        return random.choice(COLOR_LIBRARY[_fg_style])

    return random.choice([i for _, lst in COLOR_LIBRARY.items() for i in lst])


def draw_letters(
    canvas_size=None,
    fonts_dir=None,
    font_file=None,
    destination_directory=None,
    font_size=None,
    bg_color=None,
    fg_color=None,
    bg_style=None,
    fg_style=None,
    display_image=False,
):
    """
    Draw the alphabet.

    Parameters
    ----------
    canvas_size : int or None
        Length (in pixles) of square image. Defaults to `CANVAS_SIZE`.
    fonts_dir : str or None
        Absolute path to local font directory. Defaults to `FONTS_DIR`.
    font_file : str or None
        Name of font file (relative to `fonts_dir`)`. Defaults to `FONT_FILE`.
    destination_directory : str or None
        Absolute path to directory where generated images will be stored.
    font_size : int or None
        Font size image text. Defaults to `CANVAS_SIZE`.
    bg_color : str or None
        Color (in hex) of image background. Randomly generated if none supplied.
        See `_get_color()` for more details.
    fg_color : str or None
        Color (in hex) of image foreground. Randomly generated if none supplied.
        See `_get_color()` for more details.
    bg_style : str or None
        Label of background style. Randomly generated if none supplied.
        See `_get_color()` for more details.
    fg_style : str or None
        Label of foreground style. Randomly generated if none supplied.
        See `_get_color()` for more details.
    display_image : bool
        Whether to display the generated image.
    """

    if not destination_directory:
        destination_directory = (
            f"{ARTIFACTS_DIR}/{datetime.now().strftime('%Y%m%d_%H%M%S')}"
        )
    if not fonts_dir:
        fonts_dir = FONTS_DIR
    if not font_file:
        font_file = FONT_FILE
    if not canvas_size:
        canvas_size = CANVAS_SIZE
    if not font_size:
        font_size = canvas_size

    _log.info(f"Saving letters to '{destination_directory}'...")
    metadatas = dict()
    centered_imgs = []
    for letter in ascii_uppercase:
        uncentered_img, centered_img, metadata = draw_text_image(
            canvas_left=0,
            canvas_top=0,
            canvas_right=canvas_size,
            canvas_bottom=canvas_size,
            bg_color=_get_color(color=bg_color, style=bg_style, ground="bg"),
            message=letter,
            font_color=_get_color(color=fg_color, style=fg_style, ground="fg"),
            font_path=f"{fonts_dir}/{font_file}",
            font_size=font_size,
            file_dir=destination_directory,
        )
        metadatas[letter] = metadata
        with open(f"{destination_directory}/_metadata.json", "w") as outfile:
            json.dump(metadatas, outfile)
        centered_imgs.append((centered_img, letter))

    if display_image:
        images, labels = zip(*centered_imgs)
        ipyplot.plot_images(images, labels, img_width=canvas_size)
