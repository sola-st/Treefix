import ast # pragma: no cover
from typing import List, Dict, Any # pragma: no cover

node = ast.Call(func=ast.Name(id='get_ipython', ctx=ast.Load()), args=[ast.Str(s='ls')], keywords=[], lineno=1, col_offset=0) # pragma: no cover
_is_ipython_magic = lambda func: isinstance(func, ast.Name) and func.id in ('run_line_magic', 'system', 'getoutput') # pragma: no cover
_get_str_args = lambda args: [arg.s for arg in args if isinstance(arg, ast.Str)] # pragma: no cover
class NothingChanged(Exception): pass # pragma: no cover
class Mock: pass # pragma: no cover
self = type('MockSelf', (object,), {'magics': {1: []}, 'generic_visit': lambda node: None})() # pragma: no cover

import ast # pragma: no cover
from typing import List, Dict, Any # pragma: no cover
class NothingChanged(Exception): pass # pragma: no cover
class OffsetAndMagic: # pragma: no cover
    def __init__(self, col_offset: int, src: str): # pragma: no cover
        self.col_offset = col_offset # pragma: no cover
        self.src = src # pragma: no cover

class MockNode: # pragma: no cover
    def __init__(self): # pragma: no cover
        self.value = ast.Call(func=MockFunc(), args=[ast.Constant(value='ls')], keywords=[], lineno=1, col_offset=0) # pragma: no cover
class MockFunc: # pragma: no cover
    def __init__(self): # pragma: no cover
        self.attr = 'run_line_magic' # pragma: no cover
node = MockNode() # pragma: no cover
_is_ipython_magic = lambda func: hasattr(func, 'attr') and func.attr in ['run_line_magic', 'system', 'getoutput'] # pragma: no cover
_get_str_args = lambda args: [arg.value for arg in args] # pragma: no cover
self = type('MockSelf', (object,), {'magics': {1: []}, 'generic_visit': lambda self, node: None})() # pragma: no cover

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
    _l_(6285)

    args = _get_str_args(node.value.args)
    _l_(6270)
    if node.value.func.attr == "run_line_magic":
        _l_(6283)

        if args[0] == "pinfo":
            _l_(6277)

            src = f"?{args[1]}"
            _l_(6271)
        elif args[0] == "pinfo2":
            _l_(6276)

            src = f"??{args[1]}"
            _l_(6272)
        else:
            src = f"%{args[0]}"
            _l_(6273)
            if args[1]:
                _l_(6275)

                src += f" {args[1]}"
                _l_(6274)
    elif node.value.func.attr == "system":
        _l_(6282)

        src = f"!{args[0]}"
        _l_(6278)
    elif node.value.func.attr == "getoutput":
        _l_(6281)

        src = f"!!{args[0]}"
        _l_(6279)
    else:
        raise NothingChanged  # unsupported magic.
        _l_(6280)  # unsupported magic.
    self.magics[node.value.lineno].append(
        OffsetAndMagic(node.value.col_offset, src)
    )
    _l_(6284)
self.generic_visit(node)
_l_(6286)
