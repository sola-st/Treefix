from typing import List, Dict, Any, Optional # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/black/src/black/lines.py
from l3.Runtime import _l_
if not self.leaves:
    _l_(8245)

    aux = False
    _l_(8244)
    exit(aux)

# If a 'type: ignore' is attached to the end of a line, we
# can't split the line, because we can't know which of the
# subexpressions the ignore was meant to apply to.
#
# We only want this to apply to actual physical lines from the
# original source, though: we don't want the presence of a
# 'type: ignore' at the end of a multiline expression to
# justify pushing it all onto one line. Thus we
# (unfortunately) need to check the actual source lines and
# only report an unsplittable 'type: ignore' if this line was
# one line in the original code.

# Grab the first and last line numbers, skipping generated leaves
first_line = next((leaf.lineno for leaf in self.leaves if leaf.lineno != 0), 0)
_l_(8246)
last_line = next(
    (leaf.lineno for leaf in reversed(self.leaves) if leaf.lineno != 0), 0
)
_l_(8247)

if first_line == last_line:
    _l_(8252)

    # We look at the last two leaves since a comma or an
    # invisible paren could have been added at the end of the
    # line.
    for node in self.leaves[-2:]:
        _l_(8251)

        for comment in self.comments.get(id(node), []):
            _l_(8250)

            if is_type_comment(comment, " ignore"):
                _l_(8249)

                aux = True
                _l_(8248)
                exit(aux)
aux = False
_l_(8253)

exit(aux)
