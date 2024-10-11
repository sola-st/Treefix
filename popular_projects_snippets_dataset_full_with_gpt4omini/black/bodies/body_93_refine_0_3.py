from typing import Iterator, Any # pragma: no cover

def get_string_prefix(s: str) -> str:# pragma: no cover
    return s.split('.')[0] # pragma: no cover
string = 'Some example string that is f-expression' # pragma: no cover
def iter_fexpr_spans(s: str) -> Iterator[Any]:# pragma: no cover
    yield from range(len(s)) # pragma: no cover

from typing import Iterator # pragma: no cover

def get_string_prefix(s: str) -> str:# pragma: no cover
    return s.split('.')[0] # pragma: no cover
string = 'Some example string that is f-expression' # pragma: no cover
def iter_fexpr_spans(s: str) -> Iterator[str]:# pragma: no cover
    return (s[i:j] for i in range(len(s)) for j in range(i + 1, len(s) + 1)) # pragma: no cover

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
