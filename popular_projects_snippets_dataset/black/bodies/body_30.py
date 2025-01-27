# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/black/src/black/linegen.py
from l3.Runtime import _l_
"""Split line into many lines, starting with the last matching bracket pair.

    If the split was by optional parentheses, attempt splitting without them, too.
    `omit` is a collection of closing bracket IDs that shouldn't be considered for
    this split.

    Note: running this function modifies `bracket_depth` on the leaves of `line`.
    """
rhs_result = _first_right_hand_split(line, omit=omit)
_l_(17829)
aux = _maybe_split_omitting_optional_parens(
    rhs_result, line, line_length, features=features, omit=omit
)
_l_(17830)
exit(aux)
