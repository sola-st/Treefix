def get_string_prefix(s):# pragma: no cover
    return s.split()[0] if " " in s else s[:1] # pragma: no cover
string = "f'{some_var}'" # pragma: no cover
def iter_fexpr_spans(s):# pragma: no cover
    # Dummy implementation# pragma: no cover
    return [(0, 3)] # pragma: no cover

def get_string_prefix(s):# pragma: no cover
    return s.split()[0] if ' ' in s else s[:1] # pragma: no cover
string = "f'{some_var}'" # pragma: no cover
def iter_fexpr_spans(s):# pragma: no cover
    return (span for span in [(0, 3)]) # pragma: no cover

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
