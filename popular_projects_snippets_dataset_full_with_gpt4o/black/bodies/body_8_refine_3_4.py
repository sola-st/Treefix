from unittest.mock import Mock # pragma: no cover
import token # pragma: no cover

node = Mock(type=lambda: token.TYPE, value='dummy_value') # pragma: no cover
Leaf = Mock # pragma: no cover
self = type('Mock', (object,), {'current_line': Mock(bracket_tracker=Mock(any_open_brackets=lambda: False), append=lambda x: None), 'mode': Mock(preview=False, string_normalization=False), 'line': lambda: 0})() # pragma: no cover
generate_comments = lambda node, preview: [] # pragma: no cover
token = type('Mock', (object,), {'COMMENT': 1, 'STRING': 2, 'NUMBER': 3, 'TYPE': 4, 'WHITESPACE': [5, 6]})() # pragma: no cover
normalize_prefix = lambda node, inside_brackets: None # pragma: no cover
normalize_string_prefix = lambda value: value # pragma: no cover
normalize_string_quotes = lambda value: value # pragma: no cover
normalize_numeric_literal = lambda node: None # pragma: no cover
WHITESPACE = [token.WHITESPACE] # pragma: no cover

from unittest.mock import Mock # pragma: no cover
import token # pragma: no cover

class Leaf: pass # pragma: no cover
class MockBracketTracker:# pragma: no cover
    def any_open_brackets(self) -> bool:# pragma: no cover
        return False # pragma: no cover
class MockCurrentLine:# pragma: no cover
    def __init__(self):# pragma: no cover
        self.bracket_tracker = MockBracketTracker()# pragma: no cover
    def append(self, item):# pragma: no cover
        pass # pragma: no cover
class MockMode:# pragma: no cover
    preview = False# pragma: no cover
    string_normalization = False # pragma: no cover
class Base:# pragma: no cover
    def visit_default(self, node):# pragma: no cover
        pass # pragma: no cover
class MockSelf(Base):# pragma: no cover
    def __init__(self):# pragma: no cover
        self.current_line = MockCurrentLine()# pragma: no cover
        self.mode = MockMode()# pragma: no cover
    def line(self):# pragma: no cover
        return 42 # pragma: no cover
self = MockSelf() # pragma: no cover
def generate_comments(node: Leaf, preview=False):# pragma: no cover
    return [Mock(type=token.COMMENT, value="# comment") for _ in range(3)] # pragma: no cover
def normalize_prefix(node: Leaf, inside_brackets: bool):# pragma: no cover
    pass # pragma: no cover
def normalize_string_prefix(value: str) -> str:# pragma: no cover
    return value.lower() # pragma: no cover
def normalize_string_quotes(value: str) -> str:# pragma: no cover
    return value.replace('"', '\"') # pragma: no cover
def normalize_numeric_literal(node: Leaf):# pragma: no cover
    pass # pragma: no cover
WHITESPACE = {token.COMMENT} # pragma: no cover
node = Leaf() # pragma: no cover
node.type = token.STRING # pragma: no cover
node.value = 'Some value' # pragma: no cover

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
