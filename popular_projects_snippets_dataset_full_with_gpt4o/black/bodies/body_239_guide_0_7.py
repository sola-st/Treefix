from typing import Any # pragma: no cover
import token # pragma: no cover

class MockNode: # pragma: no cover
    def __init__(self, type, children=None, prefix=None, value=None): # pragma: no cover
        self.type = type # pragma: no cover
        self.children = children or [] # pragma: no cover
        self.prefix = prefix # pragma: no cover
        self.value = value # pragma: no cover
 # pragma: no cover
def type_repr(type): # pragma: no cover
    return token.tok_name.get(type, str(type)) # pragma: no cover
 # pragma: no cover
def out(message: str, fg: str = None, bold: bool = None, nl: bool = True): # pragma: no cover
    print(message) # pragma: no cover
 # pragma: no cover
mock_node1 = MockNode(type=1, children=[], prefix='prefix', value='value') # pragma: no cover
mock_node2 = MockNode(type=2, children=[mock_node1]) # pragma: no cover
mock_node = mock_node2 # pragma: no cover
 # pragma: no cover
class Visitor: # pragma: no cover
    def __init__(self): # pragma: no cover
        self.tree_depth = 0 # pragma: no cover
 # pragma: no cover
    def visit(self, node: Any): # pragma: no cover
        indent = ' ' * (2 * self.tree_depth) # pragma: no cover
        if isinstance(node, MockNode): # pragma: no cover
            _type = type_repr(node.type) # pragma: no cover
            out(f'{indent}{_type}', fg='yellow') # pragma: no cover
            self.tree_depth += 1 # pragma: no cover
            for child in node.children: # pragma: no cover
                aux = self.visit(child) # pragma: no cover
            self.tree_depth -= 1 # pragma: no cover
            out(f'{indent}/{_type}', fg='yellow', bold=False) # pragma: no cover
        else: # pragma: no cover
            _type = token.tok_name.get(node.type, str(node.type)) # pragma: no cover
            out(f'{indent}{_type}', fg='blue', nl=False) # pragma: no cover
            if node.prefix: # pragma: no cover
                out(f' {node.prefix!r}', fg='green', bold=False, nl=False) # pragma: no cover
            out(f' {node.value!r}', fg='blue', bold=False) # pragma: no cover
 # pragma: no cover
visitor = Visitor() # pragma: no cover
 # pragma: no cover
visitor.visit(mock_node) # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/black/src/black/debug.py
from l3.Runtime import _l_
indent = " " * (2 * self.tree_depth)
_l_(19281)
if isinstance(node, Node):
    _l_(19294)

    _type = type_repr(node.type)
    _l_(19282)
    out(f"{indent}{_type}", fg="yellow")
    _l_(19283)
    self.tree_depth += 1
    _l_(19284)
    for child in node.children:
        _l_(19286)

        aux = self.visit(child)
        _l_(19285)
        exit(aux)

    self.tree_depth -= 1
    _l_(19287)
    out(f"{indent}/{_type}", fg="yellow", bold=False)
    _l_(19288)
else:
    _type = token.tok_name.get(node.type, str(node.type))
    _l_(19289)
    out(f"{indent}{_type}", fg="blue", nl=False)
    _l_(19290)
    if node.prefix:
        _l_(19292)

        # We don't have to handle prefixes for `Node` objects since
        # that delegates to the first child anyway.
        out(f" {node.prefix!r}", fg="green", bold=False, nl=False)
        _l_(19291)
    out(f" {node.value!r}", fg="blue", bold=False)
    _l_(19293)
