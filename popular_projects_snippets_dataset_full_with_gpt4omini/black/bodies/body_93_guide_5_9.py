from typing import Iterator # pragma: no cover

def get_string_prefix(string: str) -> str: return 'f' # pragma: no cover
def iter_fexpr_spans(string: str) -> Iterator[int]: return iter([1, 2]) # pragma: no cover
string = 'example f-string' # pragma: no cover

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
