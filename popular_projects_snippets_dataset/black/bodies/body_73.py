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
_l_(17598)
if "f" in string_prefix:
    _l_(17600)

    string = _toggle_fexpr_quotes(string, QUOTE)
    _l_(17599)

RE_EVEN_BACKSLASHES = r"(?:(?<!\\)(?:\\\\)*)"
_l_(17601)
naked_string = string[len(string_prefix) + 1 : -1]
_l_(17602)
naked_string = re.sub(
    "(" + RE_EVEN_BACKSLASHES + ")" + QUOTE, r"\1\\" + QUOTE, naked_string
)
_l_(17603)
aux = naked_string
_l_(17604)
exit(aux)
