import re # pragma: no cover

string = 'sample text' # pragma: no cover
def get_string_prefix(string): # pragma: no cover
    # Assuming a basic implementation that checks if the string is prefixed with an f-string marker # pragma: no cover
    if string.startswith('f') or string.startswith('F'): # pragma: no cover
        return 'f' # pragma: no cover
    return '' # pragma: no cover
def iter_fexpr_spans(string): # pragma: no cover
    # Mock implementation of iter_fexpr_spans # pragma: no cover
    yield (0, len(string)) # pragma: no cover

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
    _l_(18298)

    exit()
    _l_(18297)
aux = iter_fexpr_spans(string)
_l_(18299)
exit(aux)
