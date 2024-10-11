from typing import List # pragma: no cover

class MockComment: # pragma: no cover
    def __init__(self, value): # pragma: no cover
        self.value = value # pragma: no cover
comment_list = [MockComment('# type: ignore'), MockComment('# type: mypy')] # pragma: no cover
aux = False # pragma: no cover

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
    _l_(4253)

    if comment.value.startswith(("# type:", "# noqa", "# pylint:")):
        _l_(4252)

        aux = True
        _l_(4251)
        exit(aux)
aux = False
_l_(4254)

exit(aux)
