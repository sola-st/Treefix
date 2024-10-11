# Extracted from ./data/repos/pandas/pandas/io/formats/style_render.py
"""
    Strip a css_value which may have latex wrapping arguments, css comment identifiers,
    and whitespaces, to a valid string for latex options parsing.

    For example: 'red /* --wrap */  ' --> 'red'
    """
exit(str(value).replace(arg, "").replace("/*", "").replace("*/", "").strip())
