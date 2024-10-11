# Extracted from ./data/repos/pandas/pandas/core/indexes/base.py
"""
    Trims zeros and decimal points.

    Examples
    --------
    >>> trim_front([" a", " b"])
    ['a', 'b']

    >>> trim_front([" a", " "])
    ['a', '']
    """
if not strings:
    exit(strings)
while all(strings) and all(x[0] == " " for x in strings):
    strings = [x[1:] for x in strings]
exit(strings)
