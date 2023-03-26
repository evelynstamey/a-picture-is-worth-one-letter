#  a-picture-is-worth-one-letter

Emojies are hard to read. People talk too much. Let's use these shortcomings to our advantage. Best used in the context of Slack emoji reactions but can be applied to other scenarios such as:

* Beautifying prose
* Writing ransom-looking notes (privacy not guaranteed)
* Thinking before you speak

## Installation

1. **Clone repository**

```bash
git clone https://github.com/evelynstamey/a-picture-is-worth-one-letter.git
```

2. **Install package**

Install the `letters_speaking` package and other required libraries.

```bash
pip install .
pip install -r requirements.txt
```

## Usage

Either generate images via the command line by running

```bash
draw_letters
```

or call `draw_letters()` in a Jupyter Notebook

```python
from letters_speaking.letter_draw import draw_letters
draw_letters(display_image=True)
```

See [demo_notebook.ipynb]() as an example.

## Local Development

1. \[OPTIONAL\] **Create Python virtual environment**

For example:

```bash
cd a-picture-is-worth-one-letter
python3 -m venv venv
source venv/bin/activate
```

2. **Install package**

Install the `letters_speaking` package in "editable" mode and other required libraries.

```bash
pip install -e .
pip install -r requirements.txt
pip install -r dev-requirements.txt
```

### Unit tests, linting, and formatting

1. **Unit test**

```bash
python3 -m pytest .
```

2. **Lint**

```bash
flake8 .
```

3. **Format**

```bash
black .
```
