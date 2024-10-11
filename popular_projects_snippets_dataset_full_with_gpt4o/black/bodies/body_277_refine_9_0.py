import ast # pragma: no cover

_is_ipython_magic = lambda func: func.attr in {'run_line_magic', 'system', 'getoutput'} # pragma: no cover
_get_str_args = lambda args: [arg.s for arg in args] # pragma: no cover
NothingChanged = type('NothingChanged', (Exception,), {}) # pragma: no cover
self = type('MockSelf', (object,), {'magics': {}, 'generic_visit': lambda self, node: None})() # pragma: no cover
OffsetAndMagic = lambda offset, magic: (offset, magic) # pragma: no cover

import ast # pragma: no cover

class MockNodeValueFunc: attr = 'run_line_magic' # pragma: no cover
class MockNodeValueArgs: pass # pragma: no cover
MockNodeValueArgs.s = 'ls' # pragma: no cover
MockNodeValueArgs2 = type('MockNodeValueArgs', (object,), {'s': 'pinfo'}) # pragma: no cover
node = type('MockNode', (object,), {'value': type('MockNodeValue', (object,), {'func': MockNodeValueFunc, 'args': [MockNodeValueArgs2, MockNodeValueArgs], 'lineno': 1, 'col_offset': 0})})() # pragma: no cover
_is_ipython_magic = lambda func: func.attr in {'run_line_magic', 'system', 'getoutput'} # pragma: no cover
_get_str_args = lambda args: [arg.s for arg in args] # pragma: no cover
NothingChanged = type('NothingChanged', (Exception,), {}) # pragma: no cover
self = type('MockSelf', (object,), {'magics': {1: []}, 'generic_visit': lambda self, node: None})() # pragma: no cover
OffsetAndMagic = lambda offset, magic: (offset, magic) # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/black/src/black/handle_ipynb_magics.py
from l3.Runtime import _l_
"""Look for magics in body of cell.

        For examples,

            !ls
            !!ls
            ?ls
            ??ls

        would (respectively) get transformed to

            get_ipython().system('ls')
            get_ipython().getoutput('ls')
            get_ipython().run_line_magic('pinfo', 'ls')
            get_ipython().run_line_magic('pinfo2', 'ls')

        and we look for instances of any of the latter.
        """
if isinstance(node.value, ast.Call) and _is_ipython_magic(node.value.func):
    _l_(17777)

    args = _get_str_args(node.value.args)
    _l_(17762)
    if node.value.func.attr == "run_line_magic":
        _l_(17775)

        if args[0] == "pinfo":
            _l_(17769)

            src = f"?{args[1]}"
            _l_(17763)
        elif args[0] == "pinfo2":
            _l_(17768)

            src = f"??{args[1]}"
            _l_(17764)
        else:
            src = f"%{args[0]}"
            _l_(17765)
            if args[1]:
                _l_(17767)

                src += f" {args[1]}"
                _l_(17766)
    elif node.value.func.attr == "system":
        _l_(17774)

        src = f"!{args[0]}"
        _l_(17770)
    elif node.value.func.attr == "getoutput":
        _l_(17773)

        src = f"!!{args[0]}"
        _l_(17771)
    else:
        raise NothingChanged  # unsupported magic.
        _l_(17772)  # unsupported magic.
    self.magics[node.value.lineno].append(
        OffsetAndMagic(node.value.col_offset, src)
    )
    _l_(17776)
self.generic_visit(node)
_l_(17778)
