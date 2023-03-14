import numpy as np
from PIL import ImageColor
from letters_speaking import image_draw


def test_create_bw_image_backslash():
    img = image_draw.create_bw_image(
        image_dims=(100, 50),
        bg_color="pink",
        draw_method="backslash",
        fg_color=ImageColor.getrgb("green"),
    )

    (
        extreme_pixels,
        fg_width,
        fg_height,
        left,
        top,
        right,
        bottom,
    ) = image_draw.get_extrema(np.array(img))

    assert extreme_pixels == {(1, 1), (49, 49)}
    assert fg_width == 48
    assert fg_height == 48
    assert left == 1
    assert top == 1
    assert right == 49
    assert bottom == 49


def test_create_bw_image_forwardslash():
    img = image_draw.create_bw_image(
        image_dims=(50, 100),
        bg_color="pink",
        draw_method="forwardslash",
        fg_color=ImageColor.getrgb("green"),
    )
    (
        extreme_pixels,
        fg_width,
        fg_height,
        left,
        top,
        right,
        bottom,
    ) = image_draw.get_extrema(np.array(img))
    assert extreme_pixels == {(49, 1), (1, 49)}
    assert fg_width == 48
    assert fg_height == 48
    assert left == 1
    assert top == 1
    assert right == 49
    assert bottom == 49


def test_create_bw_image_arbitrary():
    img = image_draw.create_bw_image(
        image_dims=(15, 15),
        bg_color="pink",
        draw_method="points",
        fg_color=ImageColor.getrgb("green"),
        coordinates=[(2, 1), (3, 4), (5, 10)],  # <- arbitrary coordinates
    )
    (
        extreme_pixels,
        fg_width,
        fg_height,
        left,
        top,
        right,
        bottom,
    ) = image_draw.get_extrema(np.array(img))
    assert extreme_pixels == {(2, 1), (5, 10)}
    assert fg_width == 9
    assert fg_height == 3
    assert left == 2
    assert top == 1
    assert right == 5
    assert bottom == 10
