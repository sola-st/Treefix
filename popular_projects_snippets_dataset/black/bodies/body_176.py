# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/black/src/black/lines.py
from l3.Runtime import _l_
"""See `can_omit_invisible_parens`."""
length = 4 * line.depth
_l_(18734)
seen_other_brackets = False
_l_(18735)
for _index, leaf, leaf_length in line.enumerate_with_length():
    _l_(18742)

    length += leaf_length
    _l_(18736)
    if leaf is last.opening_bracket:
        _l_(18741)

        if seen_other_brackets or length <= line_length:
            _l_(18738)

            aux = True
            _l_(18737)
            exit(aux)

    elif leaf.type in OPENING_BRACKETS:
        _l_(18740)

        # There are brackets we can further split on.
        seen_other_brackets = True
        _l_(18739)
aux = False
_l_(18743)

exit(aux)
