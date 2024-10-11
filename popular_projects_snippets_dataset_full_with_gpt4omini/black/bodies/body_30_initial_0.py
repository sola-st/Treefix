from typing import List, Any # pragma: no cover

_first_right_hand_split = lambda line, omit: (line.split('(')[0], line.split('(')[1:] if '(' in line else []) # pragma: no cover
line = 'Some text with (optional) parentheses and [brackets]' # pragma: no cover
omit = [')', ']'] # pragma: no cover
_maybe_split_omitting_optional_parens = lambda rhs_result, line, line_length, features, omit: (rhs_result, line_length, features) # pragma: no cover
line_length = len(line) # pragma: no cover
features = {'feature1': True, 'feature2': False} # pragma: no cover

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
_l_(6355)
aux = _maybe_split_omitting_optional_parens(
    rhs_result, line, line_length, features=features, omit=omit
)
_l_(6356)
exit(aux)
