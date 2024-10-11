import ast # pragma: no cover

class CellMagic:# pragma: no cover
    def __init__(self, name, params, body):# pragma: no cover
        self.name = name# pragma: no cover
        self.params = params# pragma: no cover
        self.body = body # pragma: no cover
def _is_ipython_magic(func):# pragma: no cover
    return hasattr(func, 'attr') and func.attr == 'run_cell_magic' # pragma: no cover
def _get_str_args(args):# pragma: no cover
    return [arg.s for arg in args] # pragma: no cover
node = type('MockNode', (object,), {# pragma: no cover
    'value': type('MockValue', (object,), {# pragma: no cover
        'func': type('MockFunc', (object,), {# pragma: no cover
            'attr': 'run_cell_magic'# pragma: no cover
        })(),# pragma: no cover
        'args': [# pragma: no cover
            type('MockArg', (object,), {'s': 'magic_name'})(),# pragma: no cover
            type('MockArg', (object,), {'s': 'param'})(),# pragma: no cover
            type('MockArg', (object,), {'s': 'body'})()# pragma: no cover
        ]# pragma: no cover
    })()# pragma: no cover
}) # pragma: no cover
self = type('MockSelf', (object,), {'cell_magic': None, 'generic_visit': lambda self, node: None})() # pragma: no cover

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
