import token # pragma: no cover

node = type('MockNode', (object,), {'type': token.NUMBER, 'value': '42'})() # pragma: no cover
Leaf = type('MockLeaf', (object,), {}) # pragma: no cover
self = type('MockSelf', (object,), {'current_line': type('Line', (object,), {'bracket_tracker': type('BracketTracker', (object,), {'any_open_brackets': lambda: False})(), 'append': lambda x: None})(), 'mode': type('Mode', (object,), {'preview': False, 'string_normalization': True})(), 'line': lambda: None, 'visit_default': lambda x: None})() # pragma: no cover
generate_comments = lambda node, preview: [{'type': token.COMMENT, 'value': 'Mock comment'}] # pragma: no cover
normalize_prefix = lambda node, inside_brackets: None # pragma: no cover
normalize_string_prefix = lambda value: value # pragma: no cover
normalize_string_quotes = lambda value: value # pragma: no cover
normalize_numeric_literal = lambda node: None # pragma: no cover
WHITESPACE = set() # pragma: no cover

from typing import Iterable # pragma: no cover
import token # pragma: no cover

class Leaf: pass # pragma: no cover
class MockNode(Leaf): # pragma: no cover
    def __init__(self): # pragma: no cover
        self.type = token.STRING # pragma: no cover
        self.value = 'mock_value' # pragma: no cover
node = MockNode() # pragma: no cover
def generate_comments(node: Leaf, preview: bool = False) -> Iterable[str]: # pragma: no cover
    yield 'mock_comment' # pragma: no cover
def normalize_prefix(node: Leaf, inside_brackets: bool): # pragma: no cover
    pass # pragma: no cover
def normalize_string_prefix(value: str) -> str: # pragma: no cover
    return value # pragma: no cover
def normalize_string_quotes(value: str) -> str: # pragma: no cover
    return value # pragma: no cover
def normalize_numeric_literal(node: Leaf): # pragma: no cover
    pass # pragma: no cover
token.COMMENT = 1 # pragma: no cover
token.STRING = 2 # pragma: no cover
token.NUMBER = 3 # pragma: no cover
WHITESPACE = {4, 5} # pragma: no cover
class MockCurrentLine: # pragma: no cover
    def __init__(self): # pragma: no cover
        self.bracket_tracker = type('MockBracketTracker', (object,), {'any_open_brackets': lambda self: False})() # pragma: no cover
    def append(self, item): # pragma: no cover
        pass # pragma: no cover
class MockMode: # pragma: no cover
    def __init__(self): # pragma: no cover
        self.preview = False # pragma: no cover
        self.string_normalization = True # pragma: no cover
class MockSelf: # pragma: no cover
    def __init__(self): # pragma: no cover
        self.current_line = MockCurrentLine() # pragma: no cover
        self.mode = MockMode() # pragma: no cover
    def line(self): # pragma: no cover
        pass # pragma: no cover
    def visit_default(self, node): # pragma: no cover
        pass # pragma: no cover
self = MockSelf() # pragma: no cover

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
