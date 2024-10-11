import re # pragma: no cover
from typing import Match # pragma: no cover

leaf = type('Mock', (object,), {'value': r'\u0041'})() # pragma: no cover
def get_string_prefix(text: str) -> str: return 'r' # pragma: no cover
UNICODE_ESCAPE_RE = re.compile(r'(?P<backslashes>\\*)(?:(?P<u>u[0-9A-Fa-f]{4})|(?P<U>U[0-9A-Fa-f]{8})|(?P<x>x[0-9A-Fa-f]{2})|(?P<N>N\{[^}]+\}))') # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/black/src/black/strings.py
from l3.Runtime import _l_
"""Replace hex codes in Unicode escape sequences with lowercase representation."""
text = leaf.value
_l_(18070)
prefix = get_string_prefix(text)
_l_(18071)
if "r" in prefix.lower():
    _l_(18073)

    exit()
    _l_(18072)

def replace(m: Match[str]) -> str:
    _l_(18086)

    groups = m.groupdict()
    _l_(18074)
    back_slashes = groups["backslashes"]
    _l_(18075)

    if len(back_slashes) % 2 == 0:
        _l_(18077)

        aux = back_slashes + groups["body"]
        _l_(18076)
        exit(aux)

    if groups["u"]:
        _l_(18085)

        aux = back_slashes + "u" + groups["u"].lower()
        _l_(18078)
        # \u
        exit(aux)
    elif groups["U"]:
        _l_(18084)

        aux = back_slashes + "U" + groups["U"].lower()
        _l_(18079)
        # \U
        exit(aux)
    elif groups["x"]:
        _l_(18083)

        aux = back_slashes + "x" + groups["x"].lower()
        _l_(18080)
        # \x
        exit(aux)
    else:
        assert groups["N"], f"Unexpected match: {m}"
        _l_(18081)
        aux = back_slashes + "N{" + groups["N"].upper() + "}"
        _l_(18082)
        # \N{}
        exit(aux)

leaf.value = re.sub(UNICODE_ESCAPE_RE, replace, text)
_l_(18087)
