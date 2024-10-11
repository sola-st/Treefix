def get_string_prefix(s: str) -> str:# pragma: no cover
    return s.split('.')[0] if '.' in s else s # pragma: no cover
string = 'f'  # Example string containing an 'f' for testing purposes # pragma: no cover
def iter_fexpr_spans(s: str):# pragma: no cover
    # Dummy generator that yields ranges# pragma: no cover
    for i in range(len(s)):# pragma: no cover
        yield (i, i + 1) # pragma: no cover

from typing import Iterator, Tuple # pragma: no cover

def get_string_prefix(s: str) -> str:# pragma: no cover
    return s.split()[0] if s else '' # pragma: no cover
string = 'This is an f-string: f''value''' # pragma: no cover
def iter_fexpr_spans(s: str) -> Iterator[Tuple[int, int]]:# pragma: no cover
    for i in range(len(s)):# pragma: no cover
        yield (i, i + 1) # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/black/src/black/trans.py
from l3.Runtime import _l_
"""
        Yields:
            All ranges of @string which, if @string were to be split there,
            would result in the splitting of an f-expression (which is NOT
            allowed).
        """
if "f" not in get_string_prefix(string).lower():
    _l_(6855)

    exit()
    _l_(6854)
aux = iter_fexpr_spans(string)
_l_(6856)
exit(aux)
