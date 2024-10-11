def get_string_prefix(string): return string[:1] # pragma: no cover
string = 'f-example' # pragma: no cover
def iter_fexpr_spans(string): yield (0, len(string)) # pragma: no cover

def get_string_prefix(string):# pragma: no cover
    return string[:1] # pragma: no cover
string = 'f-example' # pragma: no cover
def iter_fexpr_spans(string):# pragma: no cover
    return [(0, len(string))] # pragma: no cover

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
