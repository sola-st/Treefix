import ast # pragma: no cover
from unittest.mock import Mock # pragma: no cover

node = Mock(value=Mock(func=Mock(attr='run_cell_magic'))) # pragma: no cover
_is_ipython_magic = Mock(return_value=True) # pragma: no cover
_get_str_args = Mock(return_value=['magic_name', 'param1', 'body_code']) # pragma: no cover
self = Mock(cell_magic=None, generic_visit=Mock()) # pragma: no cover
CellMagic = Mock(return_value=None) # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/black/src/black/handle_ipynb_magics.py
from l3.Runtime import _l_
"""Find cell magic, extract header and body."""
if (
    isinstance(node.value, ast.Call)
    and _is_ipython_magic(node.value.func)
    and node.value.func.attr == "run_cell_magic"
):
    _l_(5103)

    args = _get_str_args(node.value.args)
    _l_(5101)
    self.cell_magic = CellMagic(name=args[0], params=args[1], body=args[2])
    _l_(5102)
self.generic_visit(node)
_l_(5104)
