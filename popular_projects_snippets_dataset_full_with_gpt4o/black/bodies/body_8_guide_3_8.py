import token # pragma: no cover

class Leaf:# pragma: no cover
    def __init__(self, type_value, value):# pragma: no cover
        self.type = type_value# pragma: no cover
        self.value = value # pragma: no cover
 # pragma: no cover
class BracketTracker:# pragma: no cover
    def any_open_brackets(self):# pragma: no cover
        return False # pragma: no cover
 # pragma: no cover
class CurrentLine:# pragma: no cover
    def __init__(self):# pragma: no cover
        self.bracket_tracker = BracketTracker()# pragma: no cover
        self.items = []# pragma: no cover
    def append(self, item):# pragma: no cover
        self.items.append(item)# pragma: no cover
        print(f'Appended: {item}') # pragma: no cover
 # pragma: no cover
class Super:# pragma: no cover
    def visit_default(self, node):# pragma: no cover
        return 'default visit' # pragma: no cover
 # pragma: no cover
def generate_comments(node, preview):# pragma: no cover
    # Generate a comment that is not of type COMMENT to ensure uncovered paths are executed# pragma: no cover
    return [Leaf(token.STRING, 'example comment')] # pragma: no cover
 # pragma: no cover
def normalize_prefix(node, inside_brackets):# pragma: no cover
    pass # pragma: no cover
 # pragma: no cover
def normalize_string_prefix(value):# pragma: no cover
    return value # pragma: no cover
 # pragma: no cover
def normalize_string_quotes(value):# pragma: no cover
    return value # pragma: no cover
 # pragma: no cover
def normalize_numeric_literal(node):# pragma: no cover
    pass # pragma: no cover
 # pragma: no cover
WHITESPACE = set() # pragma: no cover
 # pragma: no cover
MockType = type('Mock', (object,), {# pragma: no cover
    'current_line': CurrentLine(),# pragma: no cover
    'mode': type('Mode', (object,), {'preview': False, 'string_normalization': True})(),# pragma: no cover
    'line': lambda: 'line',# pragma: no cover
    'visit_default': Super().visit_default# pragma: no cover
}) # pragma: no cover
 # pragma: no cover
node = Leaf(token.STRING, 'example') # pragma: no cover
self = MockType() # pragma: no cover

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
