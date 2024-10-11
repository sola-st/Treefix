from typing import List # pragma: no cover
import ast # pragma: no cover
from typing import List, Tuple # pragma: no cover

src = '%matplotlib inline\nfoo' # pragma: no cover
replace_cell_magics = lambda x: (x.replace('%matplotlib inline', '25716f358c32750e'), [(x, '25716f358c32750e')]) # pragma: no cover
replace_magics = lambda x: (x.replace('%matplotlib inline', '25716f358c32750e'), [(x, '25716f358c32750e')]) # pragma: no cover
NothingChanged = type('NothingChanged', (Exception,), {}) # pragma: no cover

from typing import List, Tuple # pragma: no cover
import ast # pragma: no cover

src = '%matplotlib inline\nfoo' # pragma: no cover
Replacement = Tuple[str, str] # pragma: no cover
replacements = [] # pragma: no cover
replace_cell_magics = lambda x: (x.replace('%matplotlib inline', '25716f358c32750e'), [('cell_magic', '25716f358c32750e')]) # pragma: no cover
replace_magics = lambda x: (x, []) # pragma: no cover
NothingChanged = type('NothingChanged', (Exception,), {}) # pragma: no cover

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
_l_(4609)
try:
    _l_(4614)

    ast.parse(src)
    _l_(4610)
except SyntaxError:
    _l_(4612)

    # Might have IPython magics, will process below.
    pass
    _l_(4611)
else:
    aux = (src, replacements)
    _l_(4613)
    # Syntax is fine, nothing to mask, early return.
    exit(aux)
try:
    from IPython.core.inputtransformer2 import TransformerManager
    _l_(4616)

except ImportError:
    pass

transformer_manager = TransformerManager()
_l_(4617)
transformed = transformer_manager.transform_cell(src)
_l_(4618)
transformed, cell_magic_replacements = replace_cell_magics(transformed)
_l_(4619)
replacements += cell_magic_replacements
_l_(4620)
transformed = transformer_manager.transform_cell(transformed)
_l_(4621)
transformed, magic_replacements = replace_magics(transformed)
_l_(4622)
if len(transformed.splitlines()) != len(src.splitlines()):
    _l_(4624)

    # Multi-line magic, not supported.
    raise NothingChanged
    _l_(4623)
replacements += magic_replacements
_l_(4625)
aux = (transformed, replacements)
_l_(4626)
exit(aux)
