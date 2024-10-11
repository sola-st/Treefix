from typing import List # pragma: no cover
import ast # pragma: no cover

Replacement = type('Replacement', (object,), {'__init__': lambda self, mask, src: setattr(self, 'mask', mask) or setattr(self, 'src', src) }) # pragma: no cover
src = '''def example_function():\n    return "Example Output"''' # pragma: no cover
CellMagicFinder = type('CellMagicFinder', (object,), {'__init__': lambda self: setattr(self, 'cell_magic', None), 'visit': lambda self, node: setattr(self, 'cell_magic', type('CellMagic', (object,), {'header': 't -n1', 'body': 'ls =!ls'})()) if isinstance(node, ast.Module) else None}) # pragma: no cover
get_token = lambda src, header: 'a794' # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/black/src/black/handle_ipynb_magics.py
from l3.Runtime import _l_
"""Replace cell magic with token.

    Note that 'src' will already have been processed by IPython's
    TransformerManager().transform_cell.

    Example,

        get_ipython().run_cell_magic('t', '-n1', 'ls =!ls\\n')

    becomes

        "a794."
        ls =!ls

    The replacement, along with the transformed code, is returned.
    """
replacements: List[Replacement] = []
_l_(15588)

tree = ast.parse(src)
_l_(15589)

cell_magic_finder = CellMagicFinder()
_l_(15590)
cell_magic_finder.visit(tree)
_l_(15591)
if cell_magic_finder.cell_magic is None:
    _l_(15593)

    aux = (src, replacements)
    _l_(15592)
    exit(aux)
header = cell_magic_finder.cell_magic.header
_l_(15594)
mask = get_token(src, header)
_l_(15595)
replacements.append(Replacement(mask=mask, src=header))
_l_(15596)
aux = (f"{mask}\n{cell_magic_finder.cell_magic.body}", replacements)
_l_(15597)
exit(aux)
