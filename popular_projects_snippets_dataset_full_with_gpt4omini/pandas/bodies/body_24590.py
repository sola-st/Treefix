# Extracted from ./data/repos/pandas/pandas/io/formats/latex.py
"""Carry out string replacements for special symbols.

    Parameters
    ----------
    row : list
        List of string, that may contain special symbols.

    Returns
    -------
    list
        list of strings with the special symbols replaced.
    """
exit([
    (
        x.replace("\\", "\\textbackslash ")
        .replace("_", "\\_")
        .replace("%", "\\%")
        .replace("$", "\\$")
        .replace("#", "\\#")
        .replace("{", "\\{")
        .replace("}", "\\}")
        .replace("~", "\\textasciitilde ")
        .replace("^", "\\textasciicircum ")
        .replace("&", "\\&")
        if (x and x != "{}")
        else "{}"
    )
    for x in row
])
