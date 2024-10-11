from typing import List, Any # pragma: no cover
import token # pragma: no cover

node = type('MockNode', (object,), {'type': token.STRING, 'value': 'example_value'})() # pragma: no cover
Leaf = type('Leaf', (object,), {}) # pragma: no cover
self = type('MockSelf', (object,), {'current_line': type('MockCurrentLine', (object,), {'bracket_tracker': type('MockBracketTracker', (object,), {'any_open_brackets': lambda: True})(), 'append': lambda x: None})(), 'mode': type('MockMode', (object,), {'preview': False, 'string_normalization': True})(), 'line': lambda: 1})() # pragma: no cover
generate_comments = lambda node, preview: [type('MockComment', (object,), {'type': token.COMMENT})()] # pragma: no cover
normalize_prefix = lambda node, inside_brackets: None # pragma: no cover
normalize_string_prefix = lambda value: value.replace('example', 'sample') # pragma: no cover
normalize_string_quotes = lambda value: '"' + value + '"' # pragma: no cover
normalize_numeric_literal = lambda node: None # pragma: no cover
WHITESPACE = (token.NEWLINE, token.INDENT, token.DEDENT) # pragma: no cover

from typing import List, Any # pragma: no cover
import token # pragma: no cover

class MockNode:# pragma: no cover
    def __init__(self):# pragma: no cover
        self.type = token.STRING# pragma: no cover
        self.value = 'example_value' # pragma: no cover
class Leaf(MockNode): pass # pragma: no cover
class Mock: pass # pragma: no cover
class MockBracketTracker:# pragma: no cover
    def any_open_brackets(self):# pragma: no cover
        return True # pragma: no cover
class MockCurrentLine:# pragma: no cover
    def __init__(self):# pragma: no cover
        self.bracket_tracker = MockBracketTracker()# pragma: no cover
    def append(self, comment): pass # pragma: no cover
class MockMode:# pragma: no cover
    def __init__(self):# pragma: no cover
        self.preview = False# pragma: no cover
        self.string_normalization = True # pragma: no cover
class MockSelf:# pragma: no cover
    def __init__(self):# pragma: no cover
        self.current_line = MockCurrentLine()# pragma: no cover
        self.mode = MockMode()# pragma: no cover
    def line(self): return 0# pragma: no cover
    def visit_default(self, node): return 'default_visit' # pragma: no cover
self = MockSelf() # pragma: no cover
node = MockNode() # pragma: no cover
generate_comments = lambda node, preview: [type('MockComment', (object,), {'type': token.COMMENT})()] # pragma: no cover
normalize_prefix = lambda node, inside_brackets: None # pragma: no cover
normalize_string_prefix = lambda value: value.replace('example', 'sample') # pragma: no cover
normalize_string_quotes = lambda value: '"' + value + '"' # pragma: no cover
normalize_numeric_literal = lambda node: None # pragma: no cover
WHITESPACE = [] # pragma: no cover
token.COMMENT = 'COMMENT' # pragma: no cover
token.STRING = 'STRING' # pragma: no cover
token.NUMBER = 'NUMBER' # pragma: no cover
token.NEWLINE = 'NEWLINE' # pragma: no cover
token.INDENT = 'INDENT' # pragma: no cover
token.DEDENT = 'DEDENT' # pragma: no cover

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
