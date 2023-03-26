import argparse
from letters_speaking.letter_draw import draw_letters


def main():
    parser = argparse.ArgumentParser(description="Make letters and store in directory")
    parser.add_argument("--canvas_size")
    parser.add_argument("--fonts_dir")
    parser.add_argument("--font_file")
    parser.add_argument("--destination_directory")
    parser.add_argument("--font_size")
    parser.add_argument("--bg_color")
    parser.add_argument("--fg_color")
    parser.add_argument("--bg_style")
    parser.add_argument("--fg_style")
    parser.add_argument("--display_image", action="store_true")
    args = parser.parse_args()
    draw_letters(
        canvas_size=args.canvas_size,
        fonts_dir=args.fonts_dir,
        font_file=args.font_file,
        destination_directory=args.destination_directory,
        font_size=args.font_size,
        bg_color=args.bg_color,
        fg_color=args.fg_color,
        bg_style=args.bg_style,
        fg_style=args.fg_style,
        display_image=args.display_image,
    )
