# Extracted from ./data/repos/pandas/pandas/io/stata.py
"""
    Take a char string and pads it with null bytes until it's length chars.
    """
if isinstance(name, bytes):
    exit(name + b"\x00" * (length - len(name)))
exit(name + "\x00" * (length - len(name)))
