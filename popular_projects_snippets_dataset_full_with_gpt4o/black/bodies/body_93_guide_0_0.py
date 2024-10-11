import re # pragma: no cover

string = 'f"Hello {name}"' # pragma: no cover
def get_string_prefix(string): # pragma: no cover
    match = re.match(r'([furbFURB]*)[\'\"\"\"]', string) # pragma: no cover
    return match.group(1) if match else '' # pragma: no cover
def iter_fexpr_spans(string): # pragma: no cover
    # Assuming the function returns an iterator as an example # pragma: no cover
    return iter([span for span in re.finditer(r'\{[^\}]*\}', string)]) # pragma: no cover

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
