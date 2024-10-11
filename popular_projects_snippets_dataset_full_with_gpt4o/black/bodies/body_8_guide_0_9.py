from typing import List # pragma: no cover
import token # pragma: no cover

class BracketTracker: # pragma: no cover
    def any_open_brackets(self) -> bool: # pragma: no cover
        return True # pragma: no cover
 # pragma: no cover
class Line: # pragma: no cover
    def __init__(self): # pragma: no cover
        self.bracket_tracker = BracketTracker() # pragma: no cover
    def append(self, item): # pragma: no cover
        pass # pragma: no cover
 # pragma: no cover
def generate_comments(node, preview): # pragma: no cover
    yield {'type': token.COMMENT, 'value': '# This is a comment'} # pragma: no cover
 # pragma: no cover
def normalize_prefix(node, inside_brackets: bool): # pragma: no cover
    pass # pragma: no cover
 # pragma: no cover
def normalize_string_prefix(value: str) -> str: # pragma: no cover
    return value # pragma: no cover
 # pragma: no cover
def normalize_string_quotes(value: str) -> str: # pragma: no cover
    return value # pragma: no cover
 # pragma: no cover
def normalize_numeric_literal(node): # pragma: no cover
    pass # pragma: no cover
 # pragma: no cover
WHITESPACE = set() # pragma: no cover
 # pragma: no cover
class Leaf: # pragma: no cover
    type = token.NUMBER # pragma: no cover
    value = '123' # pragma: no cover
 # pragma: no cover
class Mode: # pragma: no cover
    preview = False # pragma: no cover
    string_normalization = True # pragma: no cover
 # pragma: no cover
class Mock: # pragma: no cover
    def __init__(self): # pragma: no cover
        self.current_line = Line() # pragma: no cover
        self.mode = Mode() # pragma: no cover
    def line(self): # pragma: no cover
        return self.current_line # pragma: no cover
    def visit_default(self, node): # pragma: no cover
        return None # pragma: no cover
 # pragma: no cover
node = Leaf() # pragma: no cover
self = Mock() # pragma: no cover

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
