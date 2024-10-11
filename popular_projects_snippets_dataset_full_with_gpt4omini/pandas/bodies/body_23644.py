# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/pandas/pandas/io/stata.py
from l3.Runtime import _l_
"""
    Takes a bytes instance and pads it with null bytes until it's length chars.
    """
if isinstance(name, str):
    _l_(8752)

    name = bytes(name, "utf-8")
    _l_(8751)
aux = name + b"\x00" * (length - len(name))
_l_(8753)
exit(aux)
