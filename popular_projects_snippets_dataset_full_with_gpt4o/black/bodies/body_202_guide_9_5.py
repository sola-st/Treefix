from typing import Set, List, Generator # pragma: no cover
from lib2to3.pytree import Leaf, Node as LN # pragma: no cover
from lib2to3.pygram import python_symbols as syms # pragma: no cover
import token # pragma: no cover

class MockLeaf(Leaf): # pragma: no cover
    def __init__(self, type, value, children=None): # pragma: no cover
        self.type = type # pragma: no cover
        self.value = value # pragma: no cover
        self.children = children if children else [] # pragma: no cover
 # pragma: no cover
class MockNode(LN): # pragma: no cover
    def __init__(self, type, children): # pragma: no cover
        self.type = type # pragma: no cover
        self.children = children # pragma: no cover
 # pragma: no cover
    MockLeaf(token.NAME, 'division') # pragma: no cover
]) # pragma: no cover
 # pragma: no cover
    None, # pragma: no cover
    MockLeaf(token.NAME, '__future__'), # pragma: no cover
    None, # pragma: no cover
]) # pragma: no cover
 # pragma: no cover
node = MockNode(syms.file_input, [ # pragma: no cover
    MockNode(syms.simple_stmt, [ # pragma: no cover
        MockLeaf(token.STRING, '"docstring"'), # pragma: no cover
        MockLeaf(token.NEWLINE, '\n') # pragma: no cover
    ]), # pragma: no cover
    mock_child_node # pragma: no cover
]) # pragma: no cover
 # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/black/src/black/__init__.py
from l3.Runtime import _l_
"""Return a set of __future__ imports in the file."""
imports: Set[str] = set()
_l_(20096)

def get_imports_from_children(children: List[LN]) -> Generator[str, None, None]:
    _l_(20109)

    for child in children:
        _l_(20108)

        if isinstance(child, Leaf):
            _l_(20107)

            if child.type == token.NAME:
                _l_(20098)

                aux = child.value
                _l_(20097)
                exit(aux)

        elif child.type == syms.import_as_name:
            _l_(20106)

            orig_name = child.children[0]
            _l_(20099)
            assert isinstance(orig_name, Leaf), "Invalid syntax parsing imports"
            _l_(20100)
            assert orig_name.type == token.NAME, "Invalid syntax parsing imports"
            _l_(20101)
            aux = orig_name.value
            _l_(20102)
            exit(aux)

        elif child.type == syms.import_as_names:
            _l_(20105)

            aux = get_imports_from_children(child.children)
            _l_(20103)
            exit(aux)

        else:
            raise AssertionError("Invalid syntax parsing imports")
            _l_(20104)

for child in node.children:
    _l_(20123)

    if child.type != syms.simple_stmt:
        _l_(20111)

        break
        _l_(20110)

    first_child = child.children[0]
    _l_(20112)
    if isinstance(first_child, Leaf):
        _l_(20122)

        # Continue looking if we see a docstring; otherwise stop.
        if (
            len(child.children) == 2
            and first_child.type == token.STRING
            and child.children[1].type == token.NEWLINE
        ):
            _l_(20114)

            continue
            _l_(20113)

        break
        _l_(20115)

    elif first_child.type == syms.import_from:
        _l_(20121)

        module_name = first_child.children[1]
        _l_(20116)
        if not isinstance(module_name, Leaf) or module_name.value != "__future__":
            _l_(20118)

            break
            _l_(20117)

        imports |= set(get_imports_from_children(first_child.children[3:]))
        _l_(20119)
    else:
        break
        _l_(20120)
aux = imports
_l_(20124)

exit(aux)
