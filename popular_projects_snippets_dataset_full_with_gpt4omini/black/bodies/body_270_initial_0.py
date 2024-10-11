import ast # pragma: no cover

node = ast.Attribute(value=ast.Call(func=ast.Name(id='get_ipython', ctx=ast.Load()), args=[], keywords=[]), attr='some_attr', ctx=ast.Load()) # pragma: no cover
ast.Attribute = type('MockAttribute', (object,), {'__init__': lambda self, value, attr, ctx: None}) # pragma: no cover
ast.Call = type('MockCall', (object,), {'__init__': lambda self, func, args, keywords: None}) # pragma: no cover
ast.Name = type('MockName', (object,), {'__init__': lambda self, id, ctx: None}) # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/black/src/black/handle_ipynb_magics.py
from l3.Runtime import _l_
"""Check if attribute is IPython magic.

    Note that the source of the abstract syntax tree
    will already have been processed by IPython's
    TransformerManager().transform_cell.
    """
aux = (
    isinstance(node, ast.Attribute)
    and isinstance(node.value, ast.Call)
    and isinstance(node.value.func, ast.Name)
    and node.value.func.id == "get_ipython"
)
_l_(6086)
exit(aux)
