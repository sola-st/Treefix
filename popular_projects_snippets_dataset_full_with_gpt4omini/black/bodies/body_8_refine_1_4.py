from dataclasses import dataclass # pragma: no cover
from typing import List, Optional, Any # pragma: no cover

class Mock: pass # pragma: no cover
token = Mock() # pragma: no cover
token.COMMENT = 'COMMENT' # pragma: no cover
token.STRING = 'STRING' # pragma: no cover
token.NUMBER = 'NUMBER' # pragma: no cover
class Leaf: pass # pragma: no cover
class Mode:  # pragma: no cover
    def __init__(self): # pragma: no cover
        self.preview = False # pragma: no cover
        self.string_normalization = False # pragma: no cover
self = Mock() # pragma: no cover
self.current_line = Mock() # pragma: no cover
self.current_line.append = lambda x: None # pragma: no cover
self.current_line.bracket_tracker = Mock() # pragma: no cover
self.current_line.bracket_tracker.any_open_brackets = lambda: True # pragma: no cover
self.mode = Mode() # pragma: no cover
def generate_comments(node: Any, preview: bool) -> List[Mock]: return [Mock()] # pragma: no cover
def normalize_prefix(node: Any, inside_brackets: bool): pass # pragma: no cover
def normalize_string_prefix(value: Any) -> Any: return value # pragma: no cover
def normalize_string_quotes(value: Any) -> Any: return value # pragma: no cover
def normalize_numeric_literal(node: Any): pass # pragma: no cover
WHITESPACE = [' '] # pragma: no cover

from dataclasses import dataclass # pragma: no cover
from typing import List, Optional, Any # pragma: no cover

class Mock: pass # pragma: no cover
token = Mock() # pragma: no cover
token.COMMENT = 'COMMENT' # pragma: no cover
token.STRING = 'STRING' # pragma: no cover
token.NUMBER = 'NUMBER' # pragma: no cover
class Leaf: pass # pragma: no cover
class Mode:  # pragma: no cover
    def __init__(self): # pragma: no cover
        self.preview = False # pragma: no cover
        self.string_normalization = False # pragma: no cover
self = Mock() # pragma: no cover
self.current_line = Mock() # pragma: no cover
self.current_line.append = lambda x: None # pragma: no cover
self.current_line.bracket_tracker = Mock() # pragma: no cover
self.current_line.bracket_tracker.any_open_brackets = lambda: True # pragma: no cover
self.mode = Mode() # pragma: no cover
node = Leaf() # pragma: no cover
node.type = token.STRING # pragma: no cover
node.value = 'example_string' # pragma: no cover
def generate_comments(node: Any, preview: bool) -> List[Mock]: return [Mock()] # pragma: no cover
def normalize_prefix(node: Any, inside_brackets: bool): pass # pragma: no cover
def normalize_string_prefix(value: Any) -> Any: return value # pragma: no cover
def normalize_string_quotes(value: Any) -> Any: return value # pragma: no cover
def normalize_numeric_literal(node: Any): pass # pragma: no cover
WHITESPACE = [' '] # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/black/src/black/linegen.py
from l3.Runtime import _l_
"""Default `visit_*()` implementation. Recurses to children of `node`."""
if isinstance(node, Leaf):
    _l_(7545)

    any_open_brackets = self.current_line.bracket_tracker.any_open_brackets()
    _l_(7527)
    for comment in generate_comments(node, preview=self.mode.preview):
        _l_(7536)

        if any_open_brackets:
            _l_(7535)

            # any comment within brackets is subject to splitting
            self.current_line.append(comment)
            _l_(7528)
        elif comment.type == token.COMMENT:
            _l_(7534)

            # regular trailing comment
            self.current_line.append(comment)
            _l_(7529)
            aux = self.line()
            _l_(7530)
            exit(aux)

        else:
            aux = self.line()
            _l_(7531)
            # regular standalone comment
            exit(aux)

            self.current_line.append(comment)
            _l_(7532)
            aux = self.line()
            _l_(7533)
            exit(aux)

    normalize_prefix(node, inside_brackets=any_open_brackets)
    _l_(7537)
    if self.mode.string_normalization and node.type == token.STRING:
        _l_(7540)

        node.value = normalize_string_prefix(node.value)
        _l_(7538)
        node.value = normalize_string_quotes(node.value)
        _l_(7539)
    if node.type == token.NUMBER:
        _l_(7542)

        normalize_numeric_literal(node)
        _l_(7541)
    if node.type not in WHITESPACE:
        _l_(7544)

        self.current_line.append(node)
        _l_(7543)
aux = super().visit_default(node)
_l_(7546)
exit(aux)
