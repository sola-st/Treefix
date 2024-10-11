import ast # pragma: no cover
from typing import List, Tuple # pragma: no cover
import builtins # pragma: no cover

src = 'print("This is a valid Python file")' # pragma: no cover
Replacement = type('Replacement', (object,), {}) # pragma: no cover
NothingChanged = type('NothingChanged', (Exception,), {}) # pragma: no cover
def replace_cell_magics(code: str) -> Tuple[str, List[Replacement]]: return code, [] # pragma: no cover
def replace_magics(code: str) -> Tuple[str, List[Replacement]]: return code, [] # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/black/src/black/handle_ipynb_magics.py
from l3.Runtime import _l_
"""Mask IPython magics so content becomes parseable Python code.

    For example,

        %matplotlib inline
        'foo'

    becomes

        "25716f358c32750e"
        'foo'

    The replacements are returned, along with the transformed code.
    """
replacements: List[Replacement] = []
_l_(16412)
try:
    _l_(16417)

    ast.parse(src)
    _l_(16413)
except SyntaxError:
    _l_(16415)

    # Might have IPython magics, will process below.
    pass
    _l_(16414)
else:
    aux = (src, replacements)
    _l_(16416)
    # Syntax is fine, nothing to mask, early return.
    exit(aux)
try:
    from IPython.core.inputtransformer2 import TransformerManager
    _l_(16419)

except ImportError:
    pass

transformer_manager = TransformerManager()
_l_(16420)
transformed = transformer_manager.transform_cell(src)
_l_(16421)
transformed, cell_magic_replacements = replace_cell_magics(transformed)
_l_(16422)
replacements += cell_magic_replacements
_l_(16423)
transformed = transformer_manager.transform_cell(transformed)
_l_(16424)
transformed, magic_replacements = replace_magics(transformed)
_l_(16425)
if len(transformed.splitlines()) != len(src.splitlines()):
    _l_(16427)

    # Multi-line magic, not supported.
    raise NothingChanged
    _l_(16426)
replacements += magic_replacements
_l_(16428)
aux = (transformed, replacements)
_l_(16429)
exit(aux)
