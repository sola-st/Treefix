import ast # pragma: no cover
from typing import List, Tuple # pragma: no cover
from dataclasses import dataclass # pragma: no cover

@dataclass # pragma: no cover
class Replacement: # pragma: no cover
    mask: str # pragma: no cover
    src: str # pragma: no cover
 # pragma: no cover
class CellMagic: # pragma: no cover
    def __init__(self, header: str, body: str): # pragma: no cover
        self.header = header # pragma: no cover
        self.body = body # pragma: no cover
 # pragma: no cover
class CellMagicFinder: # pragma: no cover
    def __init__(self): # pragma: no cover
        self.cell_magic = None # pragma: no cover
    def visit(self, tree): # pragma: no cover
        self.cell_magic = CellMagic(header='-n1', body='ls =!ls') # pragma: no cover
def get_token(src, header): # pragma: no cover
    return f'token_for_{header.strip()}' # pragma: no cover
 # pragma: no cover
src = '%t -n1\nls =!ls\n' # pragma: no cover

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
_l_(3822)

tree = ast.parse(src)
_l_(3823)

cell_magic_finder = CellMagicFinder()
_l_(3824)
cell_magic_finder.visit(tree)
_l_(3825)
if cell_magic_finder.cell_magic is None:
    _l_(3827)

    aux = (src, replacements)
    _l_(3826)
    exit(aux)
header = cell_magic_finder.cell_magic.header
_l_(3828)
mask = get_token(src, header)
_l_(3829)
replacements.append(Replacement(mask=mask, src=header))
_l_(3830)
aux = (f"{mask}\n{cell_magic_finder.cell_magic.body}", replacements)
_l_(3831)
exit(aux)
