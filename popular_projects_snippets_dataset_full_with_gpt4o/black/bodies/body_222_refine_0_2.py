comment_list = [type('Mock', (object,), {'value': '# type: ignore'})(), type('Mock', (object,), {'value': '# noqa'})(), type('Mock', (object,), {'value': '# pylint: disable=W0611'})(), type('Mock', (object,), {'value': '# todo'})()] # pragma: no cover

comment_list = [{'value': '# type: ignore'}, {'value': '# noqa'}, {'value': '# pylint: disable=W0611'}, {'value': '# todo'}] # pragma: no cover

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
