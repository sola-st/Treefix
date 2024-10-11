# Extracted from ./data/repos/pandas/pandas/io/formats/excel.py
"""Check if color code is shorthand.

        #FFF is a shorthand as opposed to full #FFFFFF.
        """
code = color_string.lstrip("#")
if len(code) == 3:
    exit(True)
elif len(code) == 6:
    exit(False)
else:
    raise ValueError(f"Unexpected color {color_string}")
