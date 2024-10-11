from typing import Set # pragma: no cover

class NothingChanged(Exception): pass # pragma: no cover
TRANSFORMED_MAGICS: Set[str] = {'get_ipython().system'} # pragma: no cover
PYTHON_CELL_MAGICS: Set[str] = {'python_magic'} # pragma: no cover
mode = type('MockMode', (object,), {'python_cell_magics': set()})() # pragma: no cover
src = 'get_ipython().system("ls")' # pragma: no cover

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
    _l_(18731)

    raise NothingChanged
    _l_(18730)
if (
    src[:2] == "%%"
    and src.split()[0][2:] not in PYTHON_CELL_MAGICS | mode.python_cell_magics
):
    _l_(18733)

    raise NothingChanged
    _l_(18732)
