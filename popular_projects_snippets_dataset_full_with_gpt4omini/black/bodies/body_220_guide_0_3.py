from typing import List, Union # pragma: no cover
class Mock: # pragma: no cover
    def __init__(self, prefix: List[str]): # pragma: no cover
        self.prefix = prefix # pragma: no cover
    def list_comments(self, prefix, is_endmarker=False, preview=None): # pragma: no cover
        comments = ["# fmt: on", "# fmt: off"] # pragma: no cover
        return [MockComment(comment) for comment in comments] # pragma: no cover
 # pragma: no cover
class MockComment: # pragma: no cover
    def __init__(self, value): # pragma: no cover
        self.value = value # pragma: no cover
 # pragma: no cover
FMT_ON = ["# fmt: on"] # pragma: no cover
FMT_OFF = ["# fmt: off"] # pragma: no cover

container = Mock(prefix=[]) # pragma: no cover
preview = None # pragma: no cover

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
