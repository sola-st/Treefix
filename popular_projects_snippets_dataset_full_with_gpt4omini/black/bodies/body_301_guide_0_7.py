from typing import List # pragma: no cover
from pycparser.c_ast import EmptyStatement, Constant, If, For # pragma: no cover
from pycparser import c_generator # pragma: no cover
from pycparser import c_parser # pragma: no cover
from pycparser import parse_file # pragma: no cover

class MockNode: pass # pragma: no cover
mock_node = MockNode() # pragma: no cover
mock_node.type = 'simple_stmt' # pragma: no cover
mock_node.children = [] # pragma: no cover
child_mock = MockNode() # pragma: no cover
child_mock.type = 'atom' # pragma: no cover
child_mock.children = [MockNode(), MockNode(), MockNode()] # pragma: no cover
for child in child_mock.children: child.type = '.' # pragma: no cover
mock_node.children.append(child_mock) # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/black/src/black/nodes.py
from l3.Runtime import _l_
"""Return True if `node` is a simple statement containing an ellipsis."""
if not isinstance(node, Node) or node.type != syms.simple_stmt:
    _l_(7917)

    aux = False
    _l_(7916)
    exit(aux)

if len(node.children) != 2:
    _l_(7919)

    aux = False
    _l_(7918)
    exit(aux)

child = node.children[0]
_l_(7920)
aux = (
    child.type == syms.atom
    and len(child.children) == 3
    and all(leaf == Leaf(token.DOT, ".") for leaf in child.children)
)
_l_(7921)
exit(aux)
