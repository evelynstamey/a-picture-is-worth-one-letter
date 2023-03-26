import seaborn as sns


def to_rgb(colors_array):
    return [(int(i * 225), int(j * 225), int(k * 225)) for i, j, k in colors_array]


COLOR_LIBRARY = {
    "very_light": [
        *to_rgb(list(sns.light_palette("#DFBFFF"))[1:4]),
        *to_rgb(list(sns.light_palette("#BFCEFF"))[1:4]),
        *to_rgb(list(sns.light_palette("#B0FFED"))[1:4]),
        *to_rgb(list(sns.light_palette("#CBFFB0"))[1:4]),
        *to_rgb(list(sns.light_palette("#FFF5B0"))[1:4]),
        *to_rgb(list(sns.light_palette("#FFCBCB"))[1:4]),
        *to_rgb(list(sns.light_palette("#FFCBF4"))[1:4]),
    ],
    "light": [
        *to_rgb(list(sns.light_palette("#D490C4"))[2:]),
        *to_rgb(list(sns.light_palette("#CFAEF0"))[2:]),
        *to_rgb(list(sns.light_palette("#AEB2F0"))[2:]),
        *to_rgb(list(sns.light_palette("#AEDCF0"))[2:]),
        *to_rgb(list(sns.light_palette("#AEF0CB"))[2:]),
        *to_rgb(list(sns.light_palette("#CDF0AE"))[2:]),
        *to_rgb(list(sns.light_palette("#F0DAAE"))[2:]),
        *to_rgb(list(sns.light_palette("#F0BDAE"))[2:]),
    ],
    "medium": [
        *to_rgb(list(sns.light_palette("#F5724B"))[3:]),
        *to_rgb(list(sns.light_palette("#F54B78"))[3:]),
        *to_rgb(list(sns.light_palette("#6569E9"))[3:]),
        *to_rgb(list(sns.light_palette("#51D1DF"))[3:]),
        *to_rgb(list(sns.light_palette("#64B083"))[3:]),
        *to_rgb(list(sns.light_palette("#7DC03A"))[3:]),
        *to_rgb(list(sns.light_palette("#E8E247"))[3:]),
        *to_rgb(list(sns.light_palette("#FFAD4E"))[3:]),
    ],
    "dark": [
        *to_rgb(list(sns.light_palette("#B5321E"))[3:]),
        *to_rgb(list(sns.light_palette("#953B5F"))[3:]),
        *to_rgb(list(sns.light_palette("#6A367A"))[3:]),
        *to_rgb(list(sns.light_palette("#103B72"))[3:]),
        *to_rgb(list(sns.light_palette("#336161"))[3:]),
        *to_rgb(list(sns.light_palette("#426E4A"))[3:]),
        *to_rgb(list(sns.light_palette("#E27900"))[3:]),
        *to_rgb(list(sns.light_palette("#00889C"))[3:]),
    ],
}

GROUNDS = [
    ("very_light", "medium"),
    ("medium", "very_light"),
    ("dark", "light"),
    ("light", "dark"),
]
