class MockLeaf:# pragma: no cover
    def __init__(self, value):# pragma: no cover
        self.value = value# pragma: no cover
# pragma: no cover
leaf = MockLeaf(value='Some text with unicode: \u0041 \U0001F600 \x61') # pragma: no cover
def get_string_prefix(s: str) -> str:# pragma: no cover
    return s[:1]  # Mock implementation that returns the first character # pragma: no cover
# pragma: no cover
UNICODE_ESCAPE_RE = r'(?P<backslashes>\\+)(?P<body>\u(?P<u>[0-9a-fA-F]{4})|\U(?P<U>[0-9a-fA-F]{8})|\x(?P<x>[0-9a-fA-F]{2})|N{{(?P<N>[^}]{{1,}})})' # pragma: no cover

import re # pragma: no cover
from typing import Match # pragma: no cover

class MockLeaf:# pragma: no cover
    def __init__(self, value):# pragma: no cover
        self.value = value# pragma: no cover
# pragma: no cover
leaf = MockLeaf('Sample text with unicode: \u03A9 and \x41') # pragma: no cover
def get_string_prefix(s: str) -> str:# pragma: no cover
    return 'r' if s.startswith('r') else '' # pragma: no cover
UNICODE_ESCAPE_RE = r'(?P<backslashes>\\*)(?P<u>u[0-9a-fA-F]{4})|(?P<U>U[0-9a-fA-F]{8})|(?P<x>x[0-9a-fA-F]{2})|(?P<N>N\{[\w\d_]+\})' # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/black/src/black/strings.py
from l3.Runtime import _l_
"""Replace hex codes in Unicode escape sequences with lowercase representation."""
text = leaf.value
_l_(6291)
prefix = get_string_prefix(text)
_l_(6292)
if "r" in prefix.lower():
    _l_(6294)

    exit()
    _l_(6293)

def replace(m: Match[str]) -> str:
    _l_(6307)

    groups = m.groupdict()
    _l_(6295)
    back_slashes = groups["backslashes"]
    _l_(6296)

    if len(back_slashes) % 2 == 0:
        _l_(6298)

        aux = back_slashes + groups["body"]
        _l_(6297)
        exit(aux)

    if groups["u"]:
        _l_(6306)

        aux = back_slashes + "u" + groups["u"].lower()
        _l_(6299)
        # \u
        exit(aux)
    elif groups["U"]:
        _l_(6305)

        aux = back_slashes + "U" + groups["U"].lower()
        _l_(6300)
        # \U
        exit(aux)
    elif groups["x"]:
        _l_(6304)

        aux = back_slashes + "x" + groups["x"].lower()
        _l_(6301)
        # \x
        exit(aux)
    else:
        assert groups["N"], f"Unexpected match: {m}"
        _l_(6302)
        aux = back_slashes + "N{" + groups["N"].upper() + "}"
        _l_(6303)
        # \N{}
        exit(aux)

leaf.value = re.sub(UNICODE_ESCAPE_RE, replace, text)
_l_(6308)
