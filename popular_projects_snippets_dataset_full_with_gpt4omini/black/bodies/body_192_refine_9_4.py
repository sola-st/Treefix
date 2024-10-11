from typing import Union # pragma: no cover
class NothingChanged(Exception): pass # pragma: no cover

TRANSFORMED_MAGICS = ['!ls'] # pragma: no cover
src = "!ls" # pragma: no cover

from typing import Set, Any # pragma: no cover

TRANSFORMED_MAGICS = ['!'] # pragma: no cover
class NothingChanged(Exception): pass # pragma: no cover
src = "!ls" # pragma: no cover
class Mock: python_cell_magics = PYTHON_CELL_MAGICS# pragma: no cover
mode = Mock() # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/black/src/black/__init__.py
from l3.Runtime import _l_
"""Check that cell does not already contain TransformerManager transformations,
    or non-Python cell magics, which might cause tokenizer_rt to break because of
    indentations.

    If a cell contains ``!ls``, then it'll be transformed to
    ``get_ipython().system('ls')``. However, if the cell originally contained
    ``get_ipython().system('ls')``, then it would get transformed in the same way:

        >>> TransformerManager().transform_cell("get_ipython().system('ls')")
        "get_ipython().system('ls')\n"
        >>> TransformerManager().transform_cell("!ls")
        "get_ipython().system('ls')\n"

    Due to the impossibility of safely roundtripping in such situations, cells
    containing transformed magics will be ignored.
    """
if any(transformed_magic in src for transformed_magic in TRANSFORMED_MAGICS):
    _l_(7253)

    raise NothingChanged
    _l_(7252)
if (
    src[:2] == "%%"
    and src.split()[0][2:] not in PYTHON_CELL_MAGICS | mode.python_cell_magics
):
    _l_(7255)

    raise NothingChanged
    _l_(7254)
