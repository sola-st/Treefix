from typing import List, Optional # pragma: no cover

def list_comments(prefix: str, is_endmarker: bool, preview: Optional[str] = None) -> List[str]: return ['# fmt: on', '# fmt: off'] # pragma: no cover

from typing import List, Any, Optional # pragma: no cover

def list_comments(prefix: str, is_endmarker: bool, preview: Optional[Any]) -> List[dict]: return [{'value': '# fmt: on'}, {'value': '# fmt: off'}] # pragma: no cover
class MockContainer: pass # pragma: no cover
container = MockContainer() # pragma: no cover
container.prefix = 'source code here' # pragma: no cover
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
