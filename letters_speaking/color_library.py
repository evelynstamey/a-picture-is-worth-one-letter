import seaborn as sns


def to_rgb(colors_array):
    return [(int(i * 225), int(j * 225), int(k * 225)) for i, j, k in colors_array]


COLOR_LIBRARY = {
    "very_light": [
        *to_rgb(list(sns.light_palette("#DFBFFF"))[1:3]),
        *to_rgb(list(sns.light_palette("#BFCEFF"))[1:3]),
        *to_rgb(list(sns.light_palette("#B0FFED"))[1:3]),
        *to_rgb(list(sns.light_palette("#CBFFB0"))[1:3]),
        *to_rgb(list(sns.light_palette("#FFF5B0"))[1:3]),
        *to_rgb(list(sns.light_palette("#FFCBCB"))[1:3]),
        *to_rgb(list(sns.light_palette("#FFCBF4"))[1:3]),
    ],
    "light": [
        *to_rgb(list(sns.light_palette("#D490C4"))[3:]),
        *to_rgb(list(sns.light_palette("#CFAEF0"))[3:]),
        *to_rgb(list(sns.light_palette("#AEB2F0"))[3:]),
        *to_rgb(list(sns.light_palette("#AEDCF0"))[3:]),
        *to_rgb(list(sns.light_palette("#AEF0CB"))[3:]),
        *to_rgb(list(sns.light_palette("#CDF0AE"))[3:]),
        *to_rgb(list(sns.light_palette("#F0DAAE"))[3:]),
        *to_rgb(list(sns.light_palette("#F0BDAE"))[3:]),
    ],
    "medium": [
        *to_rgb(list(sns.light_palette("#F5724B"))[4:]),
        *to_rgb(list(sns.light_palette("#F54B78"))[4:]),
        *to_rgb(list(sns.light_palette("#6569E9"))[4:]),
        *to_rgb(list(sns.light_palette("#51D1DF"))[4:]),
        *to_rgb(list(sns.light_palette("#64B083"))[4:]),
        *to_rgb(list(sns.light_palette("#7DC03A"))[4:]),
        *to_rgb(list(sns.light_palette("#E8E247"))[4:]),
        *to_rgb(list(sns.light_palette("#FFAD4E"))[4:]),
    ],
    "dark": [
        *to_rgb(list(sns.light_palette("#B5321E"))[4:]),
        *to_rgb(list(sns.light_palette("#953B5F"))[4:]),
        *to_rgb(list(sns.light_palette("#6A367A"))[4:]),
        *to_rgb(list(sns.light_palette("#103B72"))[4:]),
        *to_rgb(list(sns.light_palette("#336161"))[4:]),
        *to_rgb(list(sns.light_palette("#426E4A"))[4:]),
        *to_rgb(list(sns.light_palette("#E27900"))[4:]),
        *to_rgb(list(sns.light_palette("#00889C"))[4:]),
    ],
}

GROUNDS = [
    ("very_light", "medium"),
    ("medium", "very_light"),
    ("dark", "light"),
    ("light", "dark"),
]
