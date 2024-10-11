text = '10j' # pragma: no cover
def format_float_or_int_string(number):# pragma: no cover
    return float(number) if '.' in number else int(number) # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/black/src/black/numerics.py
from l3.Runtime import _l_
"""Formats a complex string like `10j`"""
number = text[:-1]
_l_(16758)
suffix = text[-1]
_l_(16759)
aux = f"{format_float_or_int_string(number)}{suffix}"
_l_(16760)
exit(aux)
