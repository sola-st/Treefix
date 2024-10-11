import ast # pragma: no cover

node = type('MockNode', (object,), {'value': type('MockValue', (object,), {'func': type('MockFunc', (object,), {'attr': 'getoutput'})(), 'args': [], 'lineno': 1, 'col_offset': 1})()})() # pragma: no cover
_is_ipython_magic = lambda x: x.attr in ['getoutput', 'run_line_magic'] # pragma: no cover
_get_str_args = lambda args: ['command', 'var'] # pragma: no cover
self = type('MockSelf', (object,), {'magics': {1: []}, 'generic_visit': lambda node: None})() # pragma: no cover
OffsetAndMagic = type('OffsetAndMagic', (object,), {'__init__': lambda self, offset, src: None}) # pragma: no cover

import ast # pragma: no cover

node = type('MockNode', (object,), {'value': type('MockValue', (object,), {'func': type('MockFunc', (object,), {'attr': 'getoutput'})(), 'args': [], 'lineno': 1, 'col_offset': 1})()})() # pragma: no cover
_is_ipython_magic = lambda x: x.attr in ['getoutput', 'run_line_magic'] # pragma: no cover
_get_str_args = lambda args: ['command', 'var'] # pragma: no cover
class MockSelf:# pragma: no cover
    def __init__(self):# pragma: no cover
        self.magics = {1: []}# pragma: no cover
    def generic_visit(self, node):# pragma: no cover
        pass# pragma: no cover
self = MockSelf() # pragma: no cover
class OffsetAndMagic:# pragma: no cover
    def __init__(self, offset, src):# pragma: no cover
        self.offset = offset# pragma: no cover
        self.src = src # pragma: no cover

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
