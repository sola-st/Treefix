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

import token # pragma: no cover

Leaf = type('Leaf', (object,), {}) # pragma: no cover
node = Leaf() # pragma: no cover
node.type = token.STRING # pragma: no cover
node.value = 'mock_value' # pragma: no cover
MockBase = type('MockBase', (object,), {'visit_default': lambda self, node: None}) # pragma: no cover
self = type('MockSelf', (MockBase,), {'current_line': type('MockCurrentLine', (object,), {'bracket_tracker': type('MockBracketTracker', (object,), {'any_open_brackets': lambda self: False})(), 'append': lambda self, item: None})(), 'mode': type('MockMode', (object,), {'preview': False, 'string_normalization': True})(), 'line': lambda self: 1})() # pragma: no cover
def generate_comments(node, preview=False): return [type('MockComment', (object,), {'type': token.COMMENT, 'value': '# comment'})()] # pragma: no cover
def normalize_prefix(node, inside_brackets): pass # pragma: no cover
def normalize_string_prefix(value): return f'normalized_prefix({value})' # pragma: no cover
def normalize_string_quotes(value): return f'"{value}"' # pragma: no cover
def normalize_numeric_literal(node): pass # pragma: no cover
WHITESPACE = {token.INDENT, token.DEDENT, token.NEWLINE} # pragma: no cover

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
