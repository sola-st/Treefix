import ast # pragma: no cover
from typing import List, Dict # pragma: no cover

class OffsetAndMagic:  # Mock class for representing an offset and a magic command # pragma: no cover
    def __init__(self, col_offset: int, src: str): # pragma: no cover
        self.col_offset = col_offset # pragma: no cover
        self.src = src # pragma: no cover
 # pragma: no cover
class Mock:  # Mock class for holding magic information # pragma: no cover
    def __init__(self): # pragma: no cover
        self.magics = {1: []} # pragma: no cover
    def generic_visit(self, node): pass # pragma: no cover
def _is_ipython_magic(func):  # Function to identify IPython magic # pragma: no cover
    return func.attr in ['getoutput', 'run_line_magic'] # pragma: no cover
def _get_str_args(args):  # Function to extract string arguments # pragma: no cover
    return [arg.s for arg in args if isinstance(arg, ast.Constant)] # pragma: no cover
 # pragma: no cover
node = Mock()  # Create a mock node # pragma: no cover
node.value = Mock()  # Create a mock value for the node # pragma: no cover
node.value.func = Mock()  # Mock function for the magic # pragma: no cover
node.value.func.attr = 'run_line_magic' # pragma: no cover
# Attribute to trigger uncovered path # pragma: no cover
node.value.args = [ast.Constant(value='env'), ast.Constant(value='value')]  # Arguments for the magic command # pragma: no cover
node.value.lineno = 1  # Line number for the node # pragma: no cover
node.value.col_offset = 0  # Column offset for the node # pragma: no cover
self = Mock()  # Create a mock for the environment context # pragma: no cover

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
