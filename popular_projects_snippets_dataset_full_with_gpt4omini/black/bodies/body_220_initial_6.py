from typing import List, Any # pragma: no cover

def list_comments(prefix: str, is_endmarker: bool, preview: Any) -> List[Any]: return [{'value': '# fmt: on'}, {'value': '# fmt: off'}, {'value': '# fmt: on'}] # pragma: no cover
container = type('MockContainer', (object,), {'prefix': 'This is a sample prefix'})() # pragma: no cover
preview = None # pragma: no cover
FMT_ON = ['# fmt: on'] # pragma: no cover
FMT_OFF = ['# fmt: off'] # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/black/src/black/comments.py
from l3.Runtime import _l_
"""Determine whether formatting is switched on within a container.
    Determined by whether the last `# fmt:` comment is `on` or `off`.
    """
fmt_on = False
_l_(4143)
for comment in list_comments(container.prefix, is_endmarker=False, preview=preview):
    _l_(4148)

    if comment.value in FMT_ON:
        _l_(4147)

        fmt_on = True
        _l_(4144)
    elif comment.value in FMT_OFF:
        _l_(4146)

        fmt_on = False
        _l_(4145)
aux = fmt_on
_l_(4149)
exit(aux)
