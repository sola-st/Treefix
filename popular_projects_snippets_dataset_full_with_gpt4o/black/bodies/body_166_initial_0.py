from typing import List # pragma: no cover

Line = type('Line', (object,), {'__init__': lambda self, mode: setattr(self, 'mode', mode), '__str__': lambda self: ''}) # pragma: no cover
self = type('MockSelf', (object,), {'mode': 'TestMode', 'before': 2, 'content_lines': ['Content line 1', 'Content line 2'], 'after': 3})() # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/black/src/black/lines.py
from l3.Runtime import _l_
empty_line = str(Line(mode=self.mode))
_l_(18914)
aux = (
    [empty_line * self.before] + self.content_lines + [empty_line * self.after]
)
_l_(18915)
exit(aux)
