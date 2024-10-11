def get_string_prefix(s: str) -> str: return s.split()[0] if s else '' # pragma: no cover
string = 'f-string example' # pragma: no cover
def iter_fexpr_spans(s: str): return [(0, 1), (1, 2), (2, 3)] # pragma: no cover

from typing import Iterator, List, Tuple # pragma: no cover

def get_string_prefix(s: str) -> str: return s.split()[0] if s else '' # pragma: no cover
string = 'f-string example' # pragma: no cover
def iter_fexpr_spans(s: str) -> Iterator[Tuple[int, int]]: yield (0, len(s)) # pragma: no cover

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
