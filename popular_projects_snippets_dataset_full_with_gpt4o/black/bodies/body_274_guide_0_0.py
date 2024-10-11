import ast # pragma: no cover
from collections import namedtuple # pragma: no cover

class MockIpythonMagic: # pragma: no cover
    @staticmethod # pragma: no cover
    def _is_ipython_magic(func): # pragma: no cover
        return hasattr(func, 'attr') and func.attr == 'run_cell_magic' # pragma: no cover
def _get_str_args(args): # pragma: no cover
    return [arg.s for arg in args if isinstance(arg, ast.Str)] # pragma: no cover
CellMagic = namedtuple('CellMagic', ['name', 'params', 'body']) # pragma: no cover
node = ast.parse('run_cell_magic("name", "params", "body")').body[0].value # pragma: no cover
self = type('Mock', (object,), {'cell_magic': None, 'generic_visit': lambda self, node: None})() # pragma: no cover

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
