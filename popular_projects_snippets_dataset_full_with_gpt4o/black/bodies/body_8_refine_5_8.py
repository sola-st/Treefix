from collections import namedtuple # pragma: no cover

Leaf = namedtuple('Leaf', []) # pragma: no cover
node = Leaf() # pragma: no cover
self = type('MockSelf', (object,), {'current_line': type('CurrentLine', (object,), {'bracket_tracker': type('BracketTracker', (object,), {'any_open_brackets': lambda: False})(), 'append': lambda x: None})(), 'mode': type('Mode', (object,), {'preview': False, 'string_normalization': False})(), 'line': lambda: None, 'visit_default': lambda x: None})() # pragma: no cover
generate_comments = lambda n, preview: [] # pragma: no cover
token = type('Token', (object,), {'COMMENT': 1, 'STRING': 2, 'NUMBER': 3})() # pragma: no cover
normalize_prefix = lambda n, inside_brackets: None # pragma: no cover
normalize_string_prefix = lambda s: s # pragma: no cover
normalize_string_quotes = lambda s: s # pragma: no cover
normalize_numeric_literal = lambda n: None # pragma: no cover
WHITESPACE = set() # pragma: no cover

import token # pragma: no cover

class Leaf: # pragma: no cover
    pass # pragma: no cover
node = Leaf() # pragma: no cover
generate_comments = lambda node, preview=False: [type('Comment', (object,), {'type': token.COMMENT})()] # pragma: no cover
def normalize_prefix(node, inside_brackets): pass # pragma: no cover
def normalize_string_prefix(string): return string # pragma: no cover
def normalize_string_quotes(string): return string # pragma: no cover
def normalize_numeric_literal(node): pass # pragma: no cover
WHITESPACE = set() # pragma: no cover
class BracketTracker: # pragma: no cover
    def any_open_brackets(self): return False # pragma: no cover
class CurrentLine: # pragma: no cover
    def __init__(self): # pragma: no cover
        self.bracket_tracker = BracketTracker() # pragma: no cover
    def append(self, item): pass # pragma: no cover
class Mode: # pragma: no cover
    preview = False # pragma: no cover
    string_normalization = True # pragma: no cover
class MockSelf: # pragma: no cover
    def __init__(self): # pragma: no cover
        self.current_line = CurrentLine() # pragma: no cover
        self.mode = Mode() # pragma: no cover
    def line(self): return None # pragma: no cover
    def visit_default(self, node): return None # pragma: no cover
self = MockSelf() # pragma: no cover
token.COMMENT = 1 # pragma: no cover
token.STRING = 2 # pragma: no cover
token.NUMBER = 3 # pragma: no cover
node.type = token.STRING # pragma: no cover
node.value = 'a string value' # pragma: no cover

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
