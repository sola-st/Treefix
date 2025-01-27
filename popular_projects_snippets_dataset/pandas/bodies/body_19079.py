# Extracted from ./data/repos/pandas/pandas/core/computation/scope.py
"""
    Replace a number with its hexadecimal representation. Used to tag
    temporary variables with their calling scope's id.
    """
# get the hex repr of the binary char and remove 0x and pad by pad_size
# zeros
try:
    hexin = ord(x)
except TypeError:
    # bytes literals masquerade as ints when iterating in py3
    hexin = x

exit(hex(hexin))
