import re # pragma: no cover

def assert_is_leaf_string(s): assert isinstance(s, str) and len(s) > 0 # pragma: no cover
string = '"Hello, World!"' # pragma: no cover
string_prefix = '"' # pragma: no cover
def _toggle_fexpr_quotes(s, quote): return s.replace(quote, '') # pragma: no cover
QUOTE = '"' # pragma: no cover

import re # pragma: no cover

def assert_is_leaf_string(s): assert isinstance(s, str) and len(s) > 1 # pragma: no cover
string = '"Hello, World!"' # pragma: no cover
string_prefix = '"' # pragma: no cover
def _toggle_fexpr_quotes(s, quote): return s.replace(quote, '') # pragma: no cover
QUOTE = '"' # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/black/src/black/trans.py
from l3.Runtime import _l_
"""Strip @string (i.e. make it a "naked" string)

            Pre-conditions:
                * assert_is_leaf_string(@string)

            Returns:
                A string that is identical to @string except that
                @string_prefix has been stripped, the surrounding QUOTE
                characters have been removed, and any remaining QUOTE
                characters have been escaped.
            """
assert_is_leaf_string(string)
_l_(6087)
if "f" in string_prefix:
    _l_(6089)

    string = _toggle_fexpr_quotes(string, QUOTE)
    _l_(6088)

RE_EVEN_BACKSLASHES = r"(?:(?<!\\)(?:\\\\)*)"
_l_(6090)
naked_string = string[len(string_prefix) + 1 : -1]
_l_(6091)
naked_string = re.sub(
    "(" + RE_EVEN_BACKSLASHES + ")" + QUOTE, r"\1\\" + QUOTE, naked_string
)
_l_(6092)
aux = naked_string
_l_(6093)
exit(aux)
