list_comments = lambda prefix, is_endmarker, preview: [{'value': '# fmt: on'}, {'value': '# fmt: off'}, {'value': '# fmt: on'}] # pragma: no cover
container = type('Mock', (object,), {'prefix': 'some_prefix'})() # pragma: no cover
preview = True # pragma: no cover
FMT_ON = {'# fmt: on'} # pragma: no cover
FMT_OFF = {'# fmt: off'} # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/black/src/black/comments.py
from l3.Runtime import _l_
"""Determine whether formatting is switched on within a container.
    Determined by whether the last `# fmt:` comment is `on` or `off`.
    """
fmt_on = False
_l_(16039)
for comment in list_comments(container.prefix, is_endmarker=False, preview=preview):
    _l_(16044)

    if comment.value in FMT_ON:
        _l_(16043)

        fmt_on = True
        _l_(16040)
    elif comment.value in FMT_OFF:
        _l_(16042)

        fmt_on = False
        _l_(16041)
aux = fmt_on
_l_(16045)
exit(aux)
