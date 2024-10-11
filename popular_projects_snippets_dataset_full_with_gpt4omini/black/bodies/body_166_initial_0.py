from typing import List # pragma: no cover

class Line:# pragma: no cover
    def __init__(self, mode):# pragma: no cover
        self.mode = mode # pragma: no cover
self = type('MockSelf', (object,), {'mode': 'test_mode', 'before': 2, 'content_lines': ['line1', 'line2'], 'after': 1})() # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/black/src/black/lines.py
from l3.Runtime import _l_
empty_line = str(Line(mode=self.mode))
_l_(7438)
aux = (
    [empty_line * self.before] + self.content_lines + [empty_line * self.after]
)
_l_(7439)
exit(aux)
