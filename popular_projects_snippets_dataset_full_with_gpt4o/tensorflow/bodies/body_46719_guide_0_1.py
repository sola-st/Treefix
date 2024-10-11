import ast # pragma: no cover
from unittest.mock import MagicMock # pragma: no cover

global_a = True # pragma: no cover
global_b = None # pragma: no cover
self = MagicMock(_parse_and_analyze=MagicMock(return_value=ast.parse('def dummy(): pass').body[0])) # pragma: no cover
self.assertHasLiveOut = MagicMock() # pragma: no cover
self.assertHasLiveIn = MagicMock() # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/pyct/static_analysis/liveness_test.py

from l3.Runtime import _l_
def test_fn(c):
    _l_(20388)

    global global_a
    _l_(20382)
    global global_b
    _l_(20383)
    if global_a:
        _l_(20386)

        global_b = c
        _l_(20384)
    else:
        global_b = c
        _l_(20385)
    aux = global_b
    _l_(20387)
    exit(aux)

node = self._parse_and_analyze(test_fn)
_l_(20389)
fn_body = node.body
_l_(20390)
self.assertHasLiveOut(fn_body[2], ('global_b',))
_l_(20391)
self.assertHasLiveIn(fn_body[2], ('global_a', 'c'))
_l_(20392)
