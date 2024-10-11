import ast # pragma: no cover
from collections import defaultdict # pragma: no cover
from typing import NamedTuple # pragma: no cover

class OffsetAndMagic(NamedTuple): # pragma: no cover
    col_offset: int # pragma: no cover
    src: str # pragma: no cover
 # pragma: no cover
def _is_ipython_magic(func): # pragma: no cover
    return hasattr(func, 'attr') and func.attr in {'getoutput', 'run_line_magic', 'unexpected_magic'} # pragma: no cover
 # pragma: no cover
def _get_str_args(args): # pragma: no cover
    return [arg.s if isinstance(arg, ast.Str) else '' for arg in args] # pragma: no cover
 # pragma: no cover
class MockSelf: # pragma: no cover
    def __init__(self): # pragma: no cover
        self.magics = defaultdict(list) # pragma: no cover
    def generic_visit(self, node): # pragma: no cover
        pass # pragma: no cover
 # pragma: no cover
self = MockSelf() # pragma: no cover
 # pragma: no cover
func = type('MockFunc', (object,), {'attr': 'unexpected_magic'}) # pragma: no cover
node_value = type('MockNodeValue', (object,), { # pragma: no cover
    'func': func, # pragma: no cover
    'args': [ast.Str(s='dummy')], # pragma: no cover
    'lineno': 1, # pragma: no cover
    'col_offset': 0 # pragma: no cover
}) # pragma: no cover
node = type('MockNode', (object,), {'value': node_value}) # pragma: no cover

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
    _l_(17840)

    args = _get_str_args(node.value.args)
    _l_(17831)
    if node.value.func.attr == "getoutput":
        _l_(17838)

        src = f"!{args[0]}"
        _l_(17832)
    elif node.value.func.attr == "run_line_magic":
        _l_(17837)

        src = f"%{args[0]}"
        _l_(17833)
        if args[1]:
            _l_(17835)

            src += f" {args[1]}"
            _l_(17834)
    else:
        raise AssertionError(
            f"Unexpected IPython magic {node.value.func.attr!r} found. "
            "Please report a bug on https://github.com/psf/black/issues."
        ) from None
        _l_(17836)
    self.magics[node.value.lineno].append(
        OffsetAndMagic(node.value.col_offset, src)
    )
    _l_(17839)
self.generic_visit(node)
_l_(17841)
