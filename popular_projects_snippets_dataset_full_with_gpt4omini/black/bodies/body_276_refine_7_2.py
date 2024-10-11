import ast # pragma: no cover
from typing import List, Dict # pragma: no cover
from unittest.mock import MagicMock # pragma: no cover

node = MagicMock(value=MagicMock(spec=ast.Call)) # pragma: no cover
ast = MagicMock() # pragma: no cover
_is_ipython_magic = MagicMock(return_value=True) # pragma: no cover
_get_str_args = MagicMock(return_value=['arg1', 'arg2']) # pragma: no cover
self = MagicMock() # pragma: no cover
OffsetAndMagic = MagicMock() # pragma: no cover
self.magics = {1: []} # pragma: no cover
node.value = MagicMock() # pragma: no cover
node.value.func = MagicMock(attr='getoutput') # pragma: no cover
node.value.lineno = 1 # pragma: no cover
node.value.col_offset = 0 # pragma: no cover
self.generic_visit = MagicMock() # pragma: no cover

import ast # pragma: no cover
from typing import List, Dict # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/black/src/black/handle_ipynb_magics.py
from l3.Runtime import _l_
"""Look for system assign magics.

        For example,

            black_version = !black --version
            env = %env var

        would have been (respectively) transformed to

            black_version = get_ipython().getoutput('black --version')
            env = get_ipython().run_line_magic('env', 'var')

        and we look for instances of any of the latter.
        """
if isinstance(node.value, ast.Call) and _is_ipython_magic(node.value.func):
    _l_(6366)

    args = _get_str_args(node.value.args)
    _l_(6357)
    if node.value.func.attr == "getoutput":
        _l_(6364)

        src = f"!{args[0]}"
        _l_(6358)
    elif node.value.func.attr == "run_line_magic":
        _l_(6363)

        src = f"%{args[0]}"
        _l_(6359)
        if args[1]:
            _l_(6361)

            src += f" {args[1]}"
            _l_(6360)
    else:
        raise AssertionError(
            f"Unexpected IPython magic {node.value.func.attr!r} found. "
            "Please report a bug on https://github.com/psf/black/issues."
        ) from None
        _l_(6362)
    self.magics[node.value.lineno].append(
        OffsetAndMagic(node.value.col_offset, src)
    )
    _l_(6365)
self.generic_visit(node)
_l_(6367)
