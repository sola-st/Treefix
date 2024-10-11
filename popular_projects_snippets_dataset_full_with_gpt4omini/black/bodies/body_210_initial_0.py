import typing # pragma: no cover
import math # pragma: no cover

text = '10j' # pragma: no cover
def format_float_or_int_string(value): return str(value) if value.isdigit() or (value[1:].isdigit() and value[0] == '-') else f'float({value})' # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/black/src/black/numerics.py
from l3.Runtime import _l_
"""Formats a complex string like `10j`"""
number = text[:-1]
_l_(5162)
suffix = text[-1]
_l_(5163)
aux = f"{format_float_or_int_string(number)}{suffix}"
_l_(5164)
exit(aux)
