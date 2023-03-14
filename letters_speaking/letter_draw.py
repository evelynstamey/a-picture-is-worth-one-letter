from letters_speaking.color_library import COLOR_LIBRARY, GROUNDS
from datetime import datetime
from IPython.display import display
from letters_speaking import image_draw
import random
from string import ascii_uppercase


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
    canvas_size,
    font_path,
    destination_directory=None,
    font_size=None,
    bg_color=None,
    fg_color=None,
    bg_style=None,
    fg_style=None,
    display_image=False,
):
    if not destination_directory:
        destination_directory = f"letters__{str(datetime.now())}"
    if not font_size:
        font_size = canvas_size

    print(f"Saving letters to '{destination_directory}'...")
    for letter in ascii_uppercase:
        uncentered_img, centered_img = image_draw.draw_text_image(
            canvas_left=0,
            canvas_top=0,
            canvas_right=canvas_size,
            canvas_bottom=canvas_size,
            bg_color=_get_color(color=bg_color, style=bg_style, ground="bg"),
            message=letter,
            font_color=_get_color(color=fg_color, style=fg_style, ground="fg"),
            font_path=font_path,
            font_size=font_size,
            file_dir=destination_directory,
        )
        if display_image:
            display(centered_img)
