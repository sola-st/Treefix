def get_string_prefix(s): # pragma: no cover
    return 'f' # pragma: no cover
string = 'Hello, {name}! How are you today?' # pragma: no cover
def iter_fexpr_spans(s): # pragma: no cover
    return [(m.start(), m.end()) for m in re.finditer(r'\{.*?\}', s)] # pragma: no cover

import re # pragma: no cover

def get_string_prefix(s): # pragma: no cover
    return 'f' # pragma: no cover
 # pragma: no cover
string = 'Hello, {name}! How are you today?' # pragma: no cover
 # pragma: no cover
def iter_fexpr_spans(s): # pragma: no cover
    return [(m.start(), m.end()) for m in re.finditer(r'\{.*?\}', s)] # pragma: no cover

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
