import ast # pragma: no cover
from typing import List, Tuple # pragma: no cover

class Replacement:# pragma: no cover
    def __init__(self, mask: str, src: str):# pragma: no cover
        self.mask = mask# pragma: no cover
        self.src = src # pragma: no cover
class MagicFinder:# pragma: no cover
    def __init__(self):# pragma: no cover
        self.magics = {}  # type: Dict[int, List[Tuple[int, str]]] # pragma: no cover
src = "%matplotlib inline\nfoo" # pragma: no cover
def get_token(source: str, magic: str) -> str:# pragma: no cover
    return '5e67db56d490fd39'  # Simulate token by hashing the magic # pragma: no cover
magic_finder = MagicFinder()  # Initialize MagicFinder instance # pragma: no cover

import ast # pragma: no cover
from typing import List, Dict, Tuple # pragma: no cover

class Replacement:# pragma: no cover
    def __init__(self, mask: str, src: str):# pragma: no cover
        self.mask = mask# pragma: no cover
        self.src = src # pragma: no cover
class MagicFinder:# pragma: no cover
    def __init__(self):# pragma: no cover
        self.magics = {}# pragma: no cover
    def visit(self, node):# pragma: no cover
        if isinstance(node, ast.Expr) and isinstance(node.value, ast.Call):# pragma: no cover
            if hasattr(node.value.func, 'id') and node.value.func.id == 'get_ipython':# pragma: no cover
                line_number = node.lineno# pragma: no cover
                if line_number not in self.magics:# pragma: no cover
                    self.magics[line_number] = []# pragma: no cover
                self.magics[line_number].append(node.value.args[0].s) # pragma: no cover
src = 'get_ipython().run_line_magic(%matplotlib, inline)\nfoo' # pragma: no cover
def get_token(src: str, magic: str) -> str:# pragma: no cover
    return '5e67db56d490fd39' # pragma: no cover
magic_finder = MagicFinder() # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/black/src/black/handle_ipynb_magics.py
from l3.Runtime import _l_
"""Replace magics within body of cell.

    Note that 'src' will already have been processed by IPython's
    TransformerManager().transform_cell.

    Example, this

        get_ipython().run_line_magic('matplotlib', 'inline')
        'foo'

    becomes

        "5e67db56d490fd39"
        'foo'

    The replacement, along with the transformed code, are returned.
    """
replacements = []
_l_(6118)
magic_finder = MagicFinder()
_l_(6119)
magic_finder.visit(ast.parse(src))
_l_(6120)
new_srcs = []
_l_(6121)
for i, line in enumerate(src.splitlines(), start=1):
    _l_(6131)

    if i in magic_finder.magics:
        _l_(6129)

        offsets_and_magics = magic_finder.magics[i]
        _l_(6122)
        if len(offsets_and_magics) != 1:
            _l_(6124)

            raise AssertionError(
                f"Expecting one magic per line, got: {offsets_and_magics}\n"
                "Please report a bug on https://github.com/psf/black/issues."
            )
            _l_(6123)
        col_offset, magic = (
            offsets_and_magics[0].col_offset,
            offsets_and_magics[0].magic,
        )
        _l_(6125)
        mask = get_token(src, magic)
        _l_(6126)
        replacements.append(Replacement(mask=mask, src=magic))
        _l_(6127)
        line = line[:col_offset] + mask
        _l_(6128)
    new_srcs.append(line)
    _l_(6130)
aux = ("\n".join(new_srcs), replacements)
_l_(6132)
exit(aux)
