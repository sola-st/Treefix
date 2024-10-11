import ast # pragma: no cover
import sys # pragma: no cover

global_a = True # pragma: no cover
global_b = None # pragma: no cover
exit = sys.exit # pragma: no cover
self = type('Mock', (object,), {'_parse_and_analyze': lambda self, fn: ast.parse(compile(fn, '', 'exec').co_consts[0]), 'assertHasLiveOut': lambda self, node, vars: None, 'assertHasLiveIn': lambda self, node, vars: None})() # pragma: no cover

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
