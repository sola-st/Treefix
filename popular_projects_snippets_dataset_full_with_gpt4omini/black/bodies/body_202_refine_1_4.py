from typing import Set, List, Generator # pragma: no cover
from typing import Callable # pragma: no cover
import token # pragma: no cover

Set = set # pragma: no cover
List = list # pragma: no cover
LN = object # pragma: no cover
Generator = callable # pragma: no cover
node = type('MockNode', (object,), {'children': []})() # pragma: no cover
syms = type('MockSyms', (object,), { # pragma: no cover
    'simple_stmt': 'simple_stmt', # pragma: no cover
})() # pragma: no cover
Leaf = type('MockLeaf', (object,), {'type': None, 'children': None, 'value': None}) # pragma: no cover
token.NAME = 'NAME' # pragma: no cover
token.STRING = 'STRING' # pragma: no cover
token.NEWLINE = 'NEWLINE' # pragma: no cover

from typing import Set, List, Generator # pragma: no cover
import token # pragma: no cover

Set = set # pragma: no cover
List = list # pragma: no cover
LN = object # pragma: no cover
Generator = callable # pragma: no cover
node = type('MockNode', (object,), {'children': []})() # pragma: no cover
syms = type('MockSyms', (object,), { # pragma: no cover
    'simple_stmt': 'simple_stmt', # pragma: no cover
})() # pragma: no cover
class Leaf:# pragma: no cover
    def __init__(self, type, value):# pragma: no cover
        self.type = type# pragma: no cover
        self.value = value# pragma: no cover
        self.children = []  # Added a children attribute for compatibility # pragma: no cover
token.NAME = 'NAME' # pragma: no cover
token.STRING = 'STRING' # pragma: no cover
token.NEWLINE = 'NEWLINE' # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/black/src/black/__init__.py
from l3.Runtime import _l_
"""Return a set of __future__ imports in the file."""
imports: Set[str] = set()
_l_(8600)

def get_imports_from_children(children: List[LN]) -> Generator[str, None, None]:
    _l_(8613)

    for child in children:
        _l_(8612)

        if isinstance(child, Leaf):
            _l_(8611)

            if child.type == token.NAME:
                _l_(8602)

                aux = child.value
                _l_(8601)
                exit(aux)

        elif child.type == syms.import_as_name:
            _l_(8610)

            orig_name = child.children[0]
            _l_(8603)
            assert isinstance(orig_name, Leaf), "Invalid syntax parsing imports"
            _l_(8604)
            assert orig_name.type == token.NAME, "Invalid syntax parsing imports"
            _l_(8605)
            aux = orig_name.value
            _l_(8606)
            exit(aux)

        elif child.type == syms.import_as_names:
            _l_(8609)

            aux = get_imports_from_children(child.children)
            _l_(8607)
            exit(aux)

        else:
            raise AssertionError("Invalid syntax parsing imports")
            _l_(8608)

for child in node.children:
    _l_(8627)

    if child.type != syms.simple_stmt:
        _l_(8615)

        break
        _l_(8614)

    first_child = child.children[0]
    _l_(8616)
    if isinstance(first_child, Leaf):
        _l_(8626)

        # Continue looking if we see a docstring; otherwise stop.
        if (
            len(child.children) == 2
            and first_child.type == token.STRING
            and child.children[1].type == token.NEWLINE
        ):
            _l_(8618)

            continue
            _l_(8617)

        break
        _l_(8619)

    elif first_child.type == syms.import_from:
        _l_(8625)

        module_name = first_child.children[1]
        _l_(8620)
        if not isinstance(module_name, Leaf) or module_name.value != "__future__":
            _l_(8622)

            break
            _l_(8621)

        imports |= set(get_imports_from_children(first_child.children[3:]))
        _l_(8623)
    else:
        break
        _l_(8624)
aux = imports
_l_(8628)

exit(aux)
