from typing import Set, List, Generator # pragma: no cover
import token # pragma: no cover

LN = type('LN', (object,), {}) # pragma: no cover
node = type('MockNode', (object,), {'children': []}) # pragma: no cover
Leaf = type('Leaf', (object,), {'__init__': lambda self, type, value: setattr(self, 'type', type) or setattr(self, 'value', value)}) # pragma: no cover
node.children = [] # pragma: no cover

from typing import Set, List, Generator # pragma: no cover
import token # pragma: no cover
from collections.abc import Iterable # pragma: no cover

LN = type('LN', (object,), {}) # pragma: no cover
class Leaf: # pragma: no cover
    def __init__(self, type, value): # pragma: no cover
        self.type = type # pragma: no cover
        self.value = value # pragma: no cover
node = type('MockNode', (object,), {'children': [type('MockChild', (object,), {'type': syms.simple_stmt, 'children': [Leaf(token.STRING, '"docstring"'), Leaf(token.NEWLINE, '\n')]})()]}) # pragma: no cover

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
