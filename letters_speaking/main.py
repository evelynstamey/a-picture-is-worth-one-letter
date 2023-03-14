import argparse
from letters_speaking.letter_draw import draw_letters


def main():
    parser = argparse.ArgumentParser(description="Make letters and store in directory")
    parser.add_argument("font_path")
    parser.add_argument("--canvas_size", default=120)

    args = parser.parse_args()
    draw_letters(
        canvas_size=args.canvas_size,
        font_path=args.font_path,
    )
