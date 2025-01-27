# Extracted from ./data/repos/pandas/pandas/io/formats/format.py
"""
    Trims trailing zeros after a decimal point,
    leaving just one if necessary.
    """
str_float = str_float.rstrip("0")
if str_float.endswith("."):
    str_float += "0"

exit(str_float)
