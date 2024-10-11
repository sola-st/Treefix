from typing import List, Generator # pragma: no cover
import token # pragma: no cover

class Leaf: pass # pragma: no cover
node = Leaf() # pragma: no cover
def generate_comments(node, preview) -> Generator[str, None, None]: yield '# comment' # pragma: no cover
token.COMMENT = 1 # pragma: no cover
token.STRING = 2 # pragma: no cover
token.NUMBER = 3 # pragma: no cover
WHITESPACE = {4, 5} # pragma: no cover
def normalize_prefix(node, inside_brackets: bool): pass # pragma: no cover
def normalize_string_prefix(value: str) -> str: return value # pragma: no cover
def normalize_string_quotes(value: str) -> str: return value # pragma: no cover
def normalize_numeric_literal(node): pass # pragma: no cover
self = type('Mock', (object,), {'current_line': type('MockLine', (object,), {'bracket_tracker': type('MockTracker', (object,), {'any_open_brackets': lambda: False})(), 'append': lambda x: None})(), 'mode': type('MockMode', (object,), {'preview': False, 'string_normalization': False})(), 'line': lambda: None, 'visit_default': lambda node: None})() # pragma: no cover

from typing import List, Generator # pragma: no cover
import token # pragma: no cover

class Leaf: pass # pragma: no cover
node = Leaf() # pragma: no cover
def generate_comments(node, preview) -> Generator[str, None, None]: yield '# comment' # pragma: no cover
token.COMMENT = 1 # pragma: no cover
token.STRING = 2 # pragma: no cover
token.NUMBER = 3 # pragma: no cover
WHITESPACE = {4, 5} # pragma: no cover
def normalize_prefix(node, inside_brackets: bool): pass # pragma: no cover
def normalize_string_prefix(value: str) -> str: return value # pragma: no cover
def normalize_string_quotes(value: str) -> str: return value # pragma: no cover
def normalize_numeric_literal(node): pass # pragma: no cover
self = type('Mock', (object,), {'current_line': type('MockLine', (object,), {'bracket_tracker': type('MockTracker', (object,), {'any_open_brackets': lambda self: False})(), 'append': lambda self, x: None})(), 'mode': type('MockMode', (object,), {'preview': False, 'string_normalization': False})(), 'line': lambda self: None, 'visit_default': lambda self, node: None})() # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/black/src/black/linegen.py
from l3.Runtime import _l_
"""Default `visit_*()` implementation. Recurses to children of `node`."""
if isinstance(node, Leaf):
    _l_(19447)

    any_open_brackets = self.current_line.bracket_tracker.any_open_brackets()
    _l_(19429)
    for comment in generate_comments(node, preview=self.mode.preview):
        _l_(19438)

        if any_open_brackets:
            _l_(19437)

            # any comment within brackets is subject to splitting
            self.current_line.append(comment)
            _l_(19430)
        elif comment.type == token.COMMENT:
            _l_(19436)

            # regular trailing comment
            self.current_line.append(comment)
            _l_(19431)
            aux = self.line()
            _l_(19432)
            exit(aux)

        else:
            aux = self.line()
            _l_(19433)
            # regular standalone comment
            exit(aux)

            self.current_line.append(comment)
            _l_(19434)
            aux = self.line()
            _l_(19435)
            exit(aux)

    normalize_prefix(node, inside_brackets=any_open_brackets)
    _l_(19439)
    if self.mode.string_normalization and node.type == token.STRING:
        _l_(19442)

        node.value = normalize_string_prefix(node.value)
        _l_(19440)
        node.value = normalize_string_quotes(node.value)
        _l_(19441)
    if node.type == token.NUMBER:
        _l_(19444)

        normalize_numeric_literal(node)
        _l_(19443)
    if node.type not in WHITESPACE:
        _l_(19446)

        self.current_line.append(node)
        _l_(19445)
aux = super().visit_default(node)
_l_(19448)
exit(aux)
