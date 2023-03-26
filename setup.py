from setuptools import setup, find_packages

setup(
    name="letters_speaking",
    version="0.0.1",
    packages=find_packages(),
    entry_points={
        "console_scripts": [
            "draw_letters = letters_speaking.main:main",
        ]
    },
)
