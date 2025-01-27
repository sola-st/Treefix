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
_l_(17597)
exit(aux)
