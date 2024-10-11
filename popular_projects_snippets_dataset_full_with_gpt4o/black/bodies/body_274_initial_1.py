import ast # pragma: no cover

node = type('Mock', (object,), {'value': type('Mock', (object,), {'func': type('Mock', (object,), {'attr': 'run_cell_magic'})()})()})() # pragma: no cover
_is_ipython_magic = lambda x: True # pragma: no cover
_get_str_args = lambda x: ['header', 'params', 'body'] # pragma: no cover
self = type('Mock', (object,), {'cell_magic': None, 'generic_visit': lambda self, node: None, 'visit': lambda self, node: None})() # pragma: no cover
CellMagic = lambda name, params, body: type('CellMagic', (object,), {'name': name, 'params': params, 'body': body})() # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/black/src/black/handle_ipynb_magics.py
from l3.Runtime import _l_
"""Find cell magic, extract header and body."""
if (
    isinstance(node.value, ast.Call)
    and _is_ipython_magic(node.value.func)
    and node.value.func.attr == "run_cell_magic"
):
    _l_(16874)

    args = _get_str_args(node.value.args)
    _l_(16872)
    self.cell_magic = CellMagic(name=args[0], params=args[1], body=args[2])
    _l_(16873)
self.generic_visit(node)
_l_(16875)
