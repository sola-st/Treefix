tail = ']' # pragma: no cover
body = '' # pragma: no cover
CannotSplit = type('CannotSplit', (Exception,), {}) # pragma: no cover

class CannotSplit(Exception): pass # pragma: no cover

tail = '' # pragma: no cover
body = 'content' # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/black/src/black/linegen.py
from l3.Runtime import _l_
"""Raise :exc:`CannotSplit` if the last left- or right-hand split failed.

    Do nothing otherwise.

    A left- or right-hand split is based on a pair of brackets. Content before
    (and including) the opening bracket is left on one line, content inside the
    brackets is put on a separate line, and finally content starting with and
    following the closing bracket is put on a separate line.

    Those are called `head`, `body`, and `tail`, respectively. If the split
    produced the same line (all content in `head`) or ended up with an empty `body`
    and the `tail` is just the closing bracket, then it's considered failed.
    """
tail_len = len(str(tail).strip())
_l_(19752)
if not body:
    _l_(19757)

    if tail_len == 0:
        _l_(19756)

        raise CannotSplit("Splitting brackets produced the same line")
        _l_(19753)

    elif tail_len < 3:
        _l_(19755)

        raise CannotSplit(
            f"Splitting brackets on an empty body to save {tail_len} characters is"
            " not worth it"
        )
        _l_(19754)
