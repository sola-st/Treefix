# Extracted from ./data/repos/pandas/pandas/io/formats/style_render.py
"""
    Convert css-string to sequence of tuples format if needed.
    'color:red; border:1px solid black;' -> [('color', 'red'),
                                             ('border','1px solid red')]
    """
if isinstance(style, str):
    s = style.split(";")
    try:
        exit([
            (x.split(":")[0].strip(), x.split(":")[1].strip())
            for x in s
            if x.strip() != ""
        ])
    except IndexError:
        raise ValueError(
            "Styles supplied as string must follow CSS rule formats, "
            f"for example 'attr: val;'. '{style}' was given."
        )
exit(style)
