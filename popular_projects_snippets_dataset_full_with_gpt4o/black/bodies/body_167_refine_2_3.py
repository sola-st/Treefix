from typing import Optional # pragma: no cover

self = type('Mock', (object,), {'_maybe_empty_lines': lambda self, line: (1, 1), 'previous_block': None, 'previous_line': None, 'mode': 'default', 'semantic_leading_comment': None})() # pragma: no cover
current_line = type('MockLine', (object,), {'is_comment': False, 'is_decorator': False})() # pragma: no cover
LinesBlock = lambda mode, previous_block, original_line, before, after: {'mode': mode, 'previous_block': previous_block, 'original_line': original_line, 'before': before, 'after': after} # pragma: no cover

from typing import Optional # pragma: no cover

class LinesBlock: # pragma: no cover
    def __init__(self, mode, previous_block, original_line, before, after): # pragma: no cover
        self.mode = mode # pragma: no cover
        self.previous_block = previous_block # pragma: no cover
        self.original_line = original_line # pragma: no cover
        self.before = before # pragma: no cover
        self.after = after # pragma: no cover
 # pragma: no cover
class MockLine: # pragma: no cover
    def __init__(self, is_comment=False, is_decorator=False): # pragma: no cover
        self.is_comment = is_comment # pragma: no cover
        self.is_decorator = is_decorator # pragma: no cover
 # pragma: no cover
self = type('Mock', (object,), { # pragma: no cover
    '_maybe_empty_lines': lambda self, line: (1, 1), # pragma: no cover
    'previous_block': None, # pragma: no cover
    'previous_line': None, # pragma: no cover
    'mode': 'default', # pragma: no cover
    'semantic_leading_comment': None # pragma: no cover
})() # pragma: no cover
 # pragma: no cover
current_line = MockLine() # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/black/src/black/lines.py
from l3.Runtime import _l_
"""Return the number of extra empty lines before and after the `current_line`.

        This is for separating `def`, `async def` and `class` with extra empty
        lines (two on module-level).
        """
before, after = self._maybe_empty_lines(current_line)
_l_(18219)
previous_after = self.previous_block.after if self.previous_block else 0
_l_(18220)
before = (
    # Black should not insert empty lines at the beginning
    # of the file
    0
    if self.previous_line is None
    else before - previous_after
)
_l_(18221)
block = LinesBlock(
    mode=self.mode,
    previous_block=self.previous_block,
    original_line=current_line,
    before=before,
    after=after,
)
_l_(18222)

# Maintain the semantic_leading_comment state.
if current_line.is_comment:
    _l_(18227)

    if self.previous_line is None or (
        not self.previous_line.is_decorator
        # `or before` means this comment already has an empty line before
        and (not self.previous_line.is_comment or before)
        and (self.semantic_leading_comment is None or before)
    ):
        _l_(18224)

        self.semantic_leading_comment = block
        _l_(18223)
elif not current_line.is_decorator or before:
    _l_(18226)

    self.semantic_leading_comment = None
    _l_(18225)

self.previous_line = current_line
_l_(18228)
self.previous_block = block
_l_(18229)
aux = block
_l_(18230)
exit(aux)
