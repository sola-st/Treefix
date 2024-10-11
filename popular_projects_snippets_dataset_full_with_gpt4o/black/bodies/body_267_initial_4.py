from typing import List # pragma: no cover
import ast # pragma: no cover

class Replacement:# pragma: no cover
    def __init__(self, mask: str, src: str):# pragma: no cover
        self.mask = mask# pragma: no cover
        self.src = src # pragma: no cover
src = """get_ipython().run_cell_magic('t', '-n1', 'ls =!ls\n')""" # pragma: no cover
class CellMagic:# pragma: no cover
    def __init__(self, header: str, body: str):# pragma: no cover
        self.header = header# pragma: no cover
        self.body = body # pragma: no cover
class CellMagicFinder(ast.NodeVisitor):# pragma: no cover
    def __init__(self):# pragma: no cover
        self.cell_magic = None# pragma: no cover
    def visit_Call(self, node):# pragma: no cover
        try:# pragma: no cover
            if (isinstance(node.func, ast.Attribute) and isinstance(node.func.value, ast.Call) and node.func.value.func.id == 'get_ipython' and node.func.attr == 'run_cell_magic'):# pragma: no cover
                header = node.args[0].s + ' ' + ' '.join(arg.s for arg in node.args[1:])# pragma: no cover
                body = node.args[2].s.replace('\\n', '\n')# pragma: no cover
                self.cell_magic = CellMagic(header=header, body=body)# pragma: no cover
        except Exception:# pragma: no cover
            pass # pragma: no cover
def get_token(src: str, header: str) -> str:# pragma: no cover
    return 'a794' # pragma: no cover

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
