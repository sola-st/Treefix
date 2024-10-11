from typing import Optional # pragma: no cover

class MockLine: pass # pragma: no cover
class MockBlock: pass # pragma: no cover
class Mock:  # pragma: no cover
    def __init__(self): # pragma: no cover
        self.previous_line = None # pragma: no cover
        self.previous_block = None # pragma: no cover
        self.mode = 'example_mode' # pragma: no cover
        self.semantic_leading_comment = None # pragma: no cover
    def _maybe_empty_lines(self, line): # pragma: no cover
        return (2, 2)  # Example values for before and after empty lines # pragma: no cover
self = Mock() # pragma: no cover
current_line = MockLine() # pragma: no cover
current_line.is_comment = False # pragma: no cover
current_line.is_decorator = False # pragma: no cover
LinesBlock = MockBlock # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/black/src/black/lines.py
from l3.Runtime import _l_
"""Return the number of extra empty lines before and after the `current_line`.

        This is for separating `def`, `async def` and `class` with extra empty
        lines (two on module-level).
        """
before, after = self._maybe_empty_lines(current_line)
_l_(6842)
previous_after = self.previous_block.after if self.previous_block else 0
_l_(6843)
before = (
    # Black should not insert empty lines at the beginning
    # of the file
    0
    if self.previous_line is None
    else before - previous_after
)
_l_(6844)
block = LinesBlock(
    mode=self.mode,
    previous_block=self.previous_block,
    original_line=current_line,
    before=before,
    after=after,
)
_l_(6845)

# Maintain the semantic_leading_comment state.
if current_line.is_comment:
    _l_(6850)

    if self.previous_line is None or (
        not self.previous_line.is_decorator
        # `or before` means this comment already has an empty line before
        and (not self.previous_line.is_comment or before)
        and (self.semantic_leading_comment is None or before)
    ):
        _l_(6847)

        self.semantic_leading_comment = block
        _l_(6846)
elif not current_line.is_decorator or before:
    _l_(6849)

    self.semantic_leading_comment = None
    _l_(6848)

self.previous_line = current_line
_l_(6851)
self.previous_block = block
_l_(6852)
aux = block
_l_(6853)
exit(aux)
