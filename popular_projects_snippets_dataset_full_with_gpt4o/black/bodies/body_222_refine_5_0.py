comment_list = [type('MockComment', (object,), {'value': '# type: ignore'}), type('MockComment', (object,), {'value': '# TODO'}), type('MockComment', (object,), {'value': '# pylint: disable=W0123'})] # pragma: no cover

class MockComment: # pragma: no cover
    def __init__(self, value): # pragma: no cover
        self.value = value # pragma: no cover
 # pragma: no cover
comment_list = [ # pragma: no cover
    MockComment('# type: ignore'), # pragma: no cover
    MockComment('# pylint: disable=W0123'), # pragma: no cover
    MockComment('# noqa'), # pragma: no cover
    MockComment('# a regular comment') # pragma: no cover
] # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/black/src/black/comments.py
from l3.Runtime import _l_
"""
    Returns:
        True iff one of the comments in @comment_list is a pragma used by one
        of the more common static analysis tools for python (e.g. mypy, flake8,
        pylint).
    """
for comment in comment_list:
    _l_(16105)

    if comment.value.startswith(("# type:", "# noqa", "# pylint:")):
        _l_(16104)

        aux = True
        _l_(16103)
        exit(aux)
aux = False
_l_(16106)

exit(aux)
