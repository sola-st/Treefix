import ast # pragma: no cover
from typing import List, Tuple # pragma: no cover
from dataclasses import dataclass # pragma: no cover

@dataclass # pragma: no cover
class Magic: # pragma: no cover
    col_offset: int # pragma: no cover
    magic: str # pragma: no cover
 # pragma: no cover
class MagicFinder(ast.NodeVisitor): # pragma: no cover
    def __init__(self): # pragma: no cover
        self.magics = {} # pragma: no cover
    def visit_Call(self, node): # pragma: no cover
        if (isinstance(node.func, ast.Attribute) and # pragma: no cover
            isinstance(node.func.value, ast.Name) and # pragma: no cover
            node.func.value.id == 'get_ipython' and # pragma: no cover
            node.func.attr == 'run_line_magic' and # pragma: no cover
            len(node.args) == 2 and # pragma: no cover
            isinstance(node.args[0], ast.Str)): # pragma: no cover
            magic_line = node.lineno # pragma: no cover
            if magic_line not in self.magics: # pragma: no cover
                self.magics[magic_line] = [] # pragma: no cover
            self.magics[magic_line].append(Magic(node.col_offset, node.args[0].s)) # pragma: no cover
        self.generic_visit(node) # pragma: no cover
 # pragma: no cover
src = ''' # pragma: no cover
get_ipython().run_line_magic('matplotlib', 'inline') # pragma: no cover
get_ipython().run_line_magic('precision', '%.2f') # pragma: no cover
''' # pragma: no cover
 # pragma: no cover
class Replacement: # pragma: no cover
    def __init__(self, mask: str, src: str): # pragma: no cover
        self.mask = mask # pragma: no cover
        self.src = src # pragma: no cover
 # pragma: no cover
def get_token(src: str, magic: str) -> str: # pragma: no cover
    # Just a simple implementation for example # pragma: no cover
    return f"***{magic}***" # pragma: no cover

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
_l_(17619)
magic_finder = MagicFinder()
_l_(17620)
magic_finder.visit(ast.parse(src))
_l_(17621)
new_srcs = []
_l_(17622)
for i, line in enumerate(src.splitlines(), start=1):
    _l_(17632)

    if i in magic_finder.magics:
        _l_(17630)

        offsets_and_magics = magic_finder.magics[i]
        _l_(17623)
        if len(offsets_and_magics) != 1:
            _l_(17625)

            raise AssertionError(
                f"Expecting one magic per line, got: {offsets_and_magics}\n"
                "Please report a bug on https://github.com/psf/black/issues."
            )
            _l_(17624)
        col_offset, magic = (
            offsets_and_magics[0].col_offset,
            offsets_and_magics[0].magic,
        )
        _l_(17626)
        mask = get_token(src, magic)
        _l_(17627)
        replacements.append(Replacement(mask=mask, src=magic))
        _l_(17628)
        line = line[:col_offset] + mask
        _l_(17629)
    new_srcs.append(line)
    _l_(17631)
aux = ("\n".join(new_srcs), replacements)
_l_(17633)
exit(aux)
