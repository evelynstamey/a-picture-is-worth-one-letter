from datetime import datetime
import logging
import numpy as np
import os
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont

logging.basicConfig(level=logging.INFO)
_log = logging.getLogger(__name__)


def get_extrema(masked_array):
    """
    Find extreme values in a 2x2 boolean array. "Extreme" values define a
    minimum bounding box that encloses all values of interest. Values of
    interest are `False` an all other values are `True`. In the context of
    `make_letters`, foreground pixels are masked to `False` and background
    pixels are masked to `True.
    """

    # get coordinates of all `False` values in a 2x2 array
    foreground_coordinates = []
    for i, row in enumerate(masked_array):
        for j, pix in enumerate(row):
            if not pix:
                foreground_coordinates.append((i, j))

    # get relevant statistics from `foreground_coordinates`
    try:
        min_i = min(i for i, _ in foreground_coordinates)
        min_j = min(j for _, j in foreground_coordinates)
        max_i = max(i for i, _ in foreground_coordinates)
        max_j = max(j for _, j in foreground_coordinates)
        extreme_pixels = set(
            [
                (i, j)
                for i, j in foreground_coordinates
                if i == min_i or j == min_j or i == max_i or j == max_j
            ]
        )
        foreground_w = max_j - min_j
        foreground_h = max_i - min_i
    except ValueError:
        _log.warning("Canvas is blank. Could not find any foreground pixels.")
        extreme_pixels = set()
        foreground_w = 0
        foreground_h = 0
        min_i = 0
        min_j = 0
        max_i = 0
        max_j = 0

    _log.debug(f"Apparent box width x height: {foreground_w} x {foreground_h}")
    _log.debug(f"Apparent box left|top|right|bottom: {min_i}|{min_j}|{max_i}|{max_j}")
    return extreme_pixels, foreground_w, foreground_h, min_i, min_j, max_i, max_j


def custom_draw(img, method, fg_color, **kwargs):
    """Generating simple images for unit testing."""
    if method == "backslash":
        _log.info("Drawing using 'backslash' method")
        width, height = img.size
        for x in range(1, min(width, height)):
            img.putpixel((x, x), fg_color)

    elif method == "forwardslash":
        _log.info("Drawing using 'forwardslash' method")
        width, height = img.size
        for x in range(1, min(width, height)):
            img.putpixel((-x, x), fg_color)

    elif method == "points":
        _log.info("Drawing using 'points' method")
        for coordinate in kwargs["coordinates"]:
            img.putpixel((coordinate[1], coordinate[0]), fg_color)

    else:
        raise Exception(f"Method '{method}' is not supported!")

    return img


def create_bw_image(
    image_dims=None, bg_color=None, draw_method=None, img=None, **draw_kwargs
):
    """# noqa
    Convert an input image to black-and-white, or generate an arbitrary image
    and convert to black-and-white.

    References
    ----------
    * https://pillow.readthedocs.io/en/stable/handbook/concepts.html#modes
    * https://pillow.readthedocs.io/en/stable/reference/Image.html#PIL.Image.Image.point
    * https://stackoverflow.com/questions/9506841/using-pil-to-turn-a-rgb-image-into-a-pure-black-and-white-image
    """
    if not img:
        _log.info("Creating new image")
        img = Image.new(mode="RGB", size=image_dims, color=bg_color)
        img = custom_draw(img, draw_method, **draw_kwargs)

    _log.debug("Converting image to black-and-white")
    # "L": 8-bit pixels, black and white
    img = img.convert(mode="L")

    # `lut`: A lookup table, containing 256 values per band in the image
    # "1": 1-bit pixels, black and white, stored with one pixel per byte
    img = img.point(lut=lambda x: 255 if x > 150 else 0, mode="1")
    return img


def draw_text_image(
    canvas_left,
    canvas_top,
    canvas_right,
    canvas_bottom,
    bg_color,
    message,
    font_path,
    font_size,
    font_color,
    file_dir,
):
    anchor_coordinates = (canvas_left, canvas_top)
    _log.debug(f"Anchor coordinates: {anchor_coordinates}")

    # get font
    font = ImageFont.truetype(font_path, font_size)

    # draw an image with given dimensions and background color
    canvas_w = canvas_right - canvas_left
    canvas_h = canvas_bottom - canvas_top
    _log.debug(f"Canvas width x height: {canvas_w} x {canvas_h}")
    uncentered_img = Image.new(mode="RGB", size=(canvas_w, canvas_h), color="white")
    draw = ImageDraw.Draw(uncentered_img)

    # draw message on image in upper left corner
    draw.text(
        xy=anchor_coordinates,  # the anchor coordinates of the text
        anchor="lt",  # specify the alignment to xy
        text=message,
        font=font,
        fill="black",
    )

    # get bounding box (in pixels) of given text relative to given anchor when
    # rendered in font; THE BOUNDING BOX INCLUDES EXTRA MARGINS FOR SOME FONTS
    bb_left, bb_top, bb_right, bb_bottom = draw.textbbox(
        xy=anchor_coordinates,  # the anchor coordinates of the text
        anchor="lt",  # specify the alignment to xy
        text=message,
        font=font,
    )
    bb_w = bb_right - bb_left
    bb_h = bb_bottom - bb_top
    _log.debug(f"Bounding box width x height: {bb_w} x {bb_h}")
    _log.debug(
        f"Bounding box left|top|right|bottom: {bb_left}|{bb_top}|{bb_right}|{bb_bottom}"
    )

    # get visual dimension of text (assumed to be smaller than the bounding box)
    # coordinates are relative to the coordinates of the bounding box
    bw_img = create_bw_image(img=uncentered_img)
    _, text_w, text_h, text_top, text_left, text_bottom, text_right = get_extrema(
        np.array(bw_img)
    )

    # get translation coordinates to center text within bounding box
    delta_w = ((bb_w / 2) + bb_left) - ((text_w / 2) + text_left)
    delta_h = ((bb_h / 2) + bb_top) - ((text_h / 2) + text_top)
    horizontal_translation = "right" if delta_w > 0 else "left"
    vertical_translation = "down" if delta_h > 0 else "up"
    _log.debug(
        f"Center text in bounding box corrections: "
        f"{horizontal_translation} {delta_w}, "
        f"{vertical_translation} {delta_h}"
    )

    # get translation coordinates to center bounding box within canvas
    center_w = ((canvas_w / 2) + canvas_left) - ((bb_w / 2) + bb_left)
    center_h = ((canvas_h / 2) + canvas_top) - ((bb_h / 2) + bb_top)
    horizontal_translation = "right" if center_w > 0 else "left"
    vertical_translation = "down" if center_h > 0 else "up"
    _log.debug(
        f"Center bounding box in canvas corrections: "
        f"{horizontal_translation} {center_w}, "
        f"{vertical_translation} {center_h}"
    )

    # draw a new image with given dimensions and background color
    centered_img = Image.new(mode="RGB", size=(canvas_w, canvas_h), color=bg_color)
    draw2 = ImageDraw.Draw(centered_img)

    # draw message on image, now centered
    adjusted_canvas_left = center_w + delta_w
    adjusted_canvas_top = center_h + delta_h
    new_anchor_coordinates = (adjusted_canvas_left, adjusted_canvas_top)
    _log.debug(f"New anchor coordinates: {new_anchor_coordinates}")
    draw2.text(
        xy=new_anchor_coordinates,  # the anchor coordinates of the text
        anchor="lt",  # specify the alignment to xy
        text=message,
        font=font,
        fill=font_color,
    )

    file_dir = file_dir if file_dir else datetime.now().strftime("%Y%m%d_%H%M%S")
    if not os.path.exists(file_dir):
        os.makedirs(file_dir)

    file_name = f"{message}.png"
    file_path = os.path.join(file_dir, file_name)
    centered_img.save(file_path, "PNG")

    metadata = {
        "canvas_left": canvas_left,
        "canvas_top": canvas_top,
        "canvas_right": canvas_right,
        "canvas_bottom": canvas_bottom,
        "bg_color": bg_color,
        "message": message,
        "font_path": font_path,
        "font_size": font_size,
        "font_color": font_color,
        "file_dir": file_dir,
        "file_name": file_name,
    }

    return uncentered_img, centered_img, metadata
